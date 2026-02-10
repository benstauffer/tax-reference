#!/usr/bin/env python3
"""
2026 US Tax Estimation Script — Standalone Calculator

Data sourced from:  YAML frontmatter in reference/tax.md
Calculation logic:  1:1 port of app/tax-map/tax-calculator.ts

Dependencies: pyyaml. Run with: python3 scripts/estimate.py
"""
import yaml
from pathlib import Path

# =============================================================================
# LOAD DATA FROM MARKDOWN FRONTMATTER
# =============================================================================

_DIR = Path(__file__).resolve().parent.parent


def _load_frontmatter(path):
    text = path.read_text()
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm)


_data = _load_frontmatter(_DIR / "reference" / "tax.md")

# Federal
FEDERAL_BRACKETS = _data["brackets"]
STANDARD_DEDUCTIONS = _data["standard_deductions"]
PAYROLL_CONFIG = _data["payroll"]
ADDITIONAL_MEDICARE_THRESHOLD = _data["additional_medicare_thresholds"]
QBID_THRESHOLDS = _data["qbid"]
SOLO_401K_LIMITS = _data["solo_401k"]
IRA_LIMIT = _data["ira_limit"]

# State
STATE_TAX_DATA = {**_data["state_no_tax"], **_data["state_flat"], **_data["state_graduated_al_mn"], **_data["state_graduated_mt_wi"]}
LOCAL_TAX_DATA = _data["local"]
CA_SCORP_ENTITY_TAX = _data["ca_scorp_entity_tax"]

STATE_STD_DEDS = {"federal_conformity": _data["federal_conformity_deductions"]}
for _key in ["state_flat_standard_deductions", "state_graduated_al_mn_standard_deductions", "state_graduated_mt_wi_standard_deductions"]:
    STATE_STD_DEDS.update(_data.get(_key, {}))

NO_TAX_STATES = _data["state_lists"]["no_tax"]
PTET_STATES = _data["state_lists"]["ptet"]
QBID_NONCONFORMING_STATES = _data["state_lists"]["qbid_nonconforming"]


# =============================================================================
# HELPER LOOKUPS
# =============================================================================

def get_federal_brackets(filing_status):
    status = "mfj" if filing_status == "qw" else filing_status
    return FEDERAL_BRACKETS.get(status, FEDERAL_BRACKETS["single"])


def get_standard_deduction(filing_status):
    return STANDARD_DEDUCTIONS.get(filing_status, STANDARD_DEDUCTIONS["single"])


def get_additional_medicare_threshold(filing_status):
    return ADDITIONAL_MEDICARE_THRESHOLD.get(filing_status, 200000)


def get_qbid_thresholds(filing_status):
    if filing_status in ("mfj", "qw"):
        return QBID_THRESHOLDS["mfj"]
    return QBID_THRESHOLDS.get(filing_status, QBID_THRESHOLDS["single"])


def get_state_standard_deduction(state_code, filing_status, agi=0):
    if state_code in NO_TAX_STATES:
        return 0
    if state_code not in STATE_TAX_DATA:
        return 0
    if state_code in STATE_STD_DEDS.get("federal_conformity", []):
        return get_standard_deduction(filing_status)
    if state_code in STATE_STD_DEDS and state_code not in ("federal_conformity",):
        state_deds = STATE_STD_DEDS[state_code]
        if isinstance(state_deds, dict):
            return state_deds.get(filing_status, state_deds.get("single", 0))
    return 0


def is_qbid_nonconforming(state_code):
    return state_code in QBID_NONCONFORMING_STATES


def has_ptet(state_code):
    return state_code in PTET_STATES


# =============================================================================
# CALCULATION FUNCTIONS (1:1 port of tax-calculator.ts)
# =============================================================================

def calculate_bracket_tax(income, brackets):
    tax = 0
    remaining = income
    details = []
    for b in brackets:
        if remaining <= 0:
            break
        bracket_max = b["max"] if b["max"] is not None else float("inf")
        bracket_size = bracket_max - b["min"]
        taxable = min(remaining, bracket_size)
        tax_in_bracket = taxable * b["rate"]
        tax += tax_in_bracket
        remaining -= taxable
        if taxable > 0:
            details.append({
                "rate": b["rate"],
                "min": b["min"],
                "max": b["max"],
                "taxable_in_bracket": round(taxable),
                "tax_in_bracket": round(tax_in_bracket),
            })
    return round(tax), details


def calculate_federal_tax(taxable_income, filing_status):
    if taxable_income <= 0:
        return 0, []
    return calculate_bracket_tax(taxable_income, get_federal_brackets(filing_status))


def calculate_state_tax(taxable_income, state_code, filing_status="single"):
    config = STATE_TAX_DATA.get(state_code)
    if not config or config["type"] == "none":
        return 0, []
    if config["type"] == "flat":
        rate = config["rate"]
        tax = round(taxable_income * rate)
        return tax, [{"rate": rate, "min": 0, "max": None, "taxable_in_bracket": taxable_income, "tax_in_bracket": tax}]
    if config["type"] == "graduated" and "brackets" in config:
        brackets = config["brackets"]
        # Brackets may be a list (same for all statuses) or a dict keyed by filing status
        if isinstance(brackets, dict):
            status = "mfj" if filing_status == "qw" else filing_status
            brackets = brackets.get(status, brackets.get("single", []))
        return calculate_bracket_tax(taxable_income, brackets)
    return 0, []


def calculate_se_tax(net_income, filing_status, other_medicare_income=0, prior_ss_wages=0):
    se_base = net_income * 0.9235
    remaining_ss = max(0, PAYROLL_CONFIG["ss_wage_base"] - prior_ss_wages)
    social_security_tax = round(min(se_base, remaining_ss) * PAYROLL_CONFIG["ss_rate"])
    medicare_tax = round(se_base * PAYROLL_CONFIG["medicare_rate"])
    remaining_threshold = max(0, get_additional_medicare_threshold(filing_status) - other_medicare_income)
    additional_medicare_tax = round(max(0, se_base - remaining_threshold) * 0.009)
    total = social_security_tax + medicare_tax + additional_medicare_tax
    return {
        "social_security_tax": social_security_tax,
        "medicare_tax": medicare_tax,
        "additional_medicare_tax": additional_medicare_tax,
        "total_se_tax": total,
        "se_deduction": round((social_security_tax + medicare_tax) / 2),
        "se_base": se_base,
    }


def calculate_payroll_tax(salary, filing_status, other_medicare_income=0, prior_ss_wages=0):
    remaining_ss = max(0, PAYROLL_CONFIG["ss_wage_base"] - prior_ss_wages)
    employer_ss = round(min(salary, remaining_ss) * PAYROLL_CONFIG["ss_rate"] / 2)
    employee_ss = round(min(salary, remaining_ss) * PAYROLL_CONFIG["ss_rate"] / 2)
    employer_medicare = round(salary * PAYROLL_CONFIG["medicare_rate"] / 2)
    employee_medicare = round(salary * PAYROLL_CONFIG["medicare_rate"] / 2)
    combined = salary + other_medicare_income
    total_over = max(0, combined - get_additional_medicare_threshold(filing_status))
    additional_medicare_on_wages = round(min(salary, total_over) * 0.009)
    return {
        "employer_ss": employer_ss,
        "employee_ss": employee_ss,
        "employer_medicare": employer_medicare,
        "employee_medicare": employee_medicare,
        "additional_medicare_on_wages": additional_medicare_on_wages,
        "total_payroll_tax": employer_ss + employee_ss + employer_medicare + employee_medicare + additional_medicare_on_wages,
    }


def calculate_qbid(qbi, taxable_before_qbid, filing_status, is_sst=False, w2_wages=0):
    t = get_qbid_thresholds(filing_status)
    threshold, phaseout_range = t["full_deduction"], t["phaseout_range"]
    max_qbid = qbi * 0.2

    if taxable_before_qbid <= threshold:
        return {"deduction": round(max_qbid), "limited_by_sstb": False, "limited_by_w2": False}

    w2_limit = w2_wages * 0.5

    if taxable_before_qbid >= threshold + phaseout_range:
        if is_sst:
            return {"deduction": 0, "limited_by_sstb": True, "limited_by_w2": False}
        ded = min(max_qbid, w2_limit)
        return {"deduction": round(ded), "limited_by_sstb": False, "limited_by_w2": ded < max_qbid}

    phaseout_pct = (taxable_before_qbid - threshold) / phaseout_range

    if is_sst:
        ded = max_qbid * (1 - phaseout_pct)
        return {"deduction": round(max(0, ded)), "limited_by_sstb": phaseout_pct > 0, "limited_by_w2": False}

    w2_limit_phase_in = w2_limit * phaseout_pct
    unlimited_portion = max_qbid * (1 - phaseout_pct)
    limited_portion = min(max_qbid * phaseout_pct, w2_limit_phase_in)
    ded = unlimited_portion + limited_portion
    return {
        "deduction": round(max(0, ded)),
        "limited_by_sstb": False,
        "limited_by_w2": limited_portion < max_qbid * phaseout_pct,
    }


def calculate_solo_401k(compensation, se_deduction, employee_deferral, employer_pct=0, age=40, is_w2=False):
    limits = SOLO_401K_LIMITS
    max_employee = limits["employee_deferral"]
    if 60 <= age <= 63:
        max_employee += limits["super_catch_up_60_63"]
    elif age >= 50:
        max_employee += limits["catch_up_50_plus"]
    employee_contrib = min(employee_deferral, max_employee)

    if is_w2:
        max_employer = round(compensation * 0.25)
        employer_contrib = round(compensation * min(employer_pct, 25) / 100)
    else:
        net_for_employer = max(0, compensation - se_deduction)
        plan_rate = min(employer_pct, 25) / 100
        reduced_rate = plan_rate / (1 + plan_rate)
        max_employer = round(net_for_employer * (0.25 / 1.25))
        employer_contrib = round(net_for_employer * reduced_rate)

    employer_contrib = min(employer_contrib, max_employer)
    total = min(employee_contrib + employer_contrib, limits["total_limit"])
    actual_employer = total - employee_contrib
    return {
        "employee_contrib": employee_contrib,
        "employer_contrib": max(0, actual_employer),
        "total_deduction": total,
        "max_employer_contrib": max_employer,
    }


def calculate_scorp_entity_taxes(net_income, gross_receipts, state_code):
    if state_code != "CA":
        return {"entity_tax": 0, "llc_fee": 0, "total": 0}
    cfg = CA_SCORP_ENTITY_TAX
    entity_tax = max(round(net_income * cfg["rate"]), cfg["minimum"])
    llc_fee = 0
    for b in cfg["llc_fee_brackets"]:
        b_max = b["max"] if b["max"] is not None else float("inf")
        if b["min"] <= gross_receipts <= b_max:
            llc_fee = b["fee"]
            break
    return {"entity_tax": entity_tax, "llc_fee": llc_fee, "total": entity_tax + llc_fee}


def calculate_spouse_employment(spouse_w2, filing_status):
    if spouse_w2 <= 0 or filing_status not in ("mfj", "qw"):
        return {"employer_payroll": 0, "employee_payroll": 0, "total_payroll_tax": 0}
    ss_wage_base = PAYROLL_CONFIG["ss_wage_base"]
    employer_payroll = round(min(spouse_w2, ss_wage_base) * PAYROLL_CONFIG["ss_rate"] / 2 + spouse_w2 * PAYROLL_CONFIG["medicare_rate"] / 2)
    employee_payroll = round(min(spouse_w2, ss_wage_base) * PAYROLL_CONFIG["ss_rate"] / 2 + spouse_w2 * PAYROLL_CONFIG["medicare_rate"] / 2)
    return {"employer_payroll": employer_payroll, "employee_payroll": employee_payroll, "total_payroll_tax": employer_payroll + employee_payroll}


def calculate_external_w2_taxes(external_w2s, filing_status, prior_ss=0, prior_medicare=0):
    if not external_w2s:
        return {"total_wages": 0, "total_ss_wages": 0, "total_401k": 0,
                "total_after_tax_401k": 0, "details": [], "total_payroll_tax": 0}
    ss_wage_base = PAYROLL_CONFIG["ss_wage_base"]
    threshold = get_additional_medicare_threshold(filing_status)
    limits = SOLO_401K_LIMITS

    details, total_wages, total_ss_wages, total_401k = [], 0, 0, 0
    total_after_tax_401k, total_payroll_tax = 0, 0
    cumulative_ss, cumulative_med = prior_ss, prior_medicare

    for w2 in external_w2s:
        wages = w2.get("wages", 0)
        contrib_401k = w2.get("contribution_401k", 0)
        after_tax_req = w2.get("after_tax_401k", 0)
        total_wages += wages
        total_401k += contrib_401k
        after_tax = min(after_tax_req, max(0, limits["total_limit"] - contrib_401k))
        total_after_tax_401k += after_tax
        remaining_ss = max(0, ss_wage_base - cumulative_ss)
        ss_wages_this = min(wages, remaining_ss)
        ss_tax = round(ss_wages_this * PAYROLL_CONFIG["ss_rate"] / 2)
        cumulative_ss += ss_wages_this
        total_ss_wages += ss_wages_this
        med_tax = round(wages * PAYROLL_CONFIG["medicare_rate"] / 2)
        income_after = cumulative_med + wages
        add_med = round(max(0, min(wages, income_after - threshold)) * 0.009) if income_after > threshold else 0
        cumulative_med += wages
        payroll_this = ss_tax + med_tax + add_med
        total_payroll_tax += payroll_this
        details.append({"label": w2.get("label", "W-2"), "wages": wages, "contribution_401k": contrib_401k,
                         "after_tax_401k": after_tax, "social_security_tax": ss_tax, "medicare_tax": med_tax,
                         "additional_medicare_tax": add_med, "total_payroll_tax": payroll_this})
    return {"total_wages": total_wages, "total_ss_wages": total_ss_wages, "total_401k": total_401k,
            "total_after_tax_401k": total_after_tax_401k, "details": details, "total_payroll_tax": total_payroll_tax}


def calculate_local_tax(income, city_code, entity_type):
    if not city_code:
        return 0
    cfg = LOCAL_TAX_DATA.get(city_code)
    return round(income * cfg["rate"]) if cfg else 0


def get_federal_marginal_rate(taxable_income, filing_status):
    for b in get_federal_brackets(filing_status):
        if taxable_income <= (b["max"] if b["max"] is not None else float("inf")):
            return b["rate"]
    return get_federal_brackets(filing_status)[-1]["rate"]


# =============================================================================
# MAIN ORCHESTRATOR (matches tax-calculator.ts calculateTaxes lines 461-878)
# =============================================================================

def calculate_taxes(inputs):
    gross_revenue = inputs.get("gross_revenue", 0)
    business_expenses = inputs.get("business_expenses", 0)
    filing_status = inputs.get("filing_status", "single")
    state_code = inputs.get("state_code", "CA")
    city_code = inputs.get("city_code", None)
    entity_type = inputs.get("entity_type", "sole_prop")
    reasonable_salary = inputs.get("reasonable_salary", 0)
    is_sst = inputs.get("is_sst", False)
    elect_ptet = inputs.get("elect_ptet", False)
    solo_401k_employee = inputs.get("solo_401k_employee", 0)
    employer_401k_percent = inputs.get("employer_401k_percent", 0)
    after_tax_401k = inputs.get("after_tax_401k", 0)
    hsa_contribution = inputs.get("hsa_contribution", 0)
    backdoor_roth = inputs.get("backdoor_roth", 0)
    se_health_insurance = inputs.get("se_health_insurance", 0)
    scorp_health_insurance = inputs.get("scorp_health_insurance", 0)
    hire_spouse = inputs.get("hire_spouse", False)
    spouse_w2 = inputs.get("spouse_w2", 0)
    spouse_401k_employee = inputs.get("spouse_401k_employee", 0)
    spouse_after_tax_401k = inputs.get("spouse_after_tax_401k", 0)
    spouse_backdoor_roth = inputs.get("spouse_backdoor_roth", 0)
    age = inputs.get("age", 40)
    external_w2s = inputs.get("external_w2s", [])

    net_business_income = max(0, gross_revenue - business_expenses)
    standard_deduction = get_standard_deduction(filing_status)

    b = {
        "gross_revenue": gross_revenue, "business_expenses": business_expenses,
        "net_business_income": net_business_income,
        "social_security_tax": 0, "medicare_tax": 0, "additional_medicare_tax": 0, "total_se_tax": 0,
        "employer_ss": 0, "employee_ss": 0, "employer_medicare": 0, "employee_medicare": 0,
        "additional_medicare_on_wages": 0, "total_payroll_tax": 0,
        "federal_tax": 0, "state_tax": 0, "local_tax": 0,
        "standard_deduction": standard_deduction, "se_deduction": 0,
        "se_health_insurance_deduction": 0, "qbid_deduction": 0,
        "hsa_deduction": hsa_contribution, "total_deductions": 0,
        "adjusted_gross_income": 0, "taxable_income": 0,
        "total_tax": 0, "take_home": 0, "take_home_cash": 0, "effective_rate": 0,
        "salary": 0, "distributions": 0, "k1_income": 0,
        "scorp_entity_tax": 0, "scorp_llc_fee": 0, "scorp_health_insurance_deduction": 0,
        "federal_tax_details": [], "state_tax_details": [],
        "ptet_tax": 0, "ptet_credit": 0, "ptet_net_benefit": 0,
        "solo_401k_employee_contrib": 0, "solo_401k_employer_contrib": 0,
        "solo_401k_deduction": 0, "after_tax_401k_contrib": 0,
        "backdoor_roth_contrib": 0, "spouse_backdoor_roth_contrib": 0,
        "spouse_payroll_tax": 0, "spouse_employer_payroll": 0, "spouse_employee_payroll": 0,
        "spouse_401k_employee_contrib": 0, "spouse_401k_employer_contrib": 0,
        "spouse_401k_deduction": 0, "spouse_after_tax_401k_contrib": 0,
        "qbid_limited_by_sstb": False, "qbid_limited_by_w2": False,
        "state_qbid_adjustment": 0, "state_taxable_income": 0, "state_standard_deduction": 0,
        "external_w2_total": 0, "external_w2_401k": 0,
        "external_w2_after_tax_401k": 0, "external_w2_details": [],
        "california_sdi": 0, "utah_tax_credit": 0,
    }

    if net_business_income <= 0 and not external_w2s:
        return b

    # Spouse employment
    spouse_result = {"employer_payroll": 0, "employee_payroll": 0, "total_payroll_tax": 0}
    effective_spouse_w2 = spouse_w2 if hire_spouse else 0
    if effective_spouse_w2 > 0 and filing_status in ("mfj", "qw"):
        spouse_result = calculate_spouse_employment(effective_spouse_w2, filing_status)
        b["spouse_payroll_tax"] = spouse_result["total_payroll_tax"]
        b["spouse_employer_payroll"] = spouse_result["employer_payroll"]
        b["spouse_employee_payroll"] = spouse_result["employee_payroll"]
        if spouse_401k_employee > 0 or employer_401k_percent > 0:
            sp_401k = calculate_solo_401k(effective_spouse_w2, 0, spouse_401k_employee, employer_401k_percent, age, True)
            b["spouse_401k_employee_contrib"] = sp_401k["employee_contrib"]
            b["spouse_401k_employer_contrib"] = sp_401k["employer_contrib"]
            b["spouse_401k_deduction"] = sp_401k["total_deduction"]
        if spouse_after_tax_401k > 0:
            sp_pre = b["spouse_401k_employee_contrib"] + b["spouse_401k_employer_contrib"]
            b["spouse_after_tax_401k_contrib"] = min(spouse_after_tax_401k, max(0, SOLO_401K_LIMITS["total_limit"] - sp_pre))

    spouse_employer_costs = spouse_result["employer_payroll"] + b["spouse_401k_employer_contrib"]
    business_income = max(0, net_business_income - effective_spouse_w2 - spouse_employer_costs)

    # External W-2s
    ext_result = calculate_external_w2_taxes(external_w2s, filing_status, 0, 0)
    b["external_w2_total"] = ext_result["total_wages"]
    b["external_w2_401k"] = ext_result["total_401k"]
    b["external_w2_after_tax_401k"] = ext_result["total_after_tax_401k"]
    b["external_w2_details"] = ext_result["details"]
    external_ss_wages = ext_result["total_ss_wages"]
    external_medicare_income = ext_result["total_wages"]

    if entity_type == "sole_prop":
        other_medicare = effective_spouse_w2 + external_medicare_income

        se = calculate_se_tax(business_income, filing_status, other_medicare, external_ss_wages)
        b["social_security_tax"] = se["social_security_tax"]
        b["medicare_tax"] = se["medicare_tax"]
        b["additional_medicare_tax"] = se["additional_medicare_tax"]
        b["total_se_tax"] = se["total_se_tax"]
        b["se_deduction"] = se["se_deduction"]

        if solo_401k_employee > 0 or employer_401k_percent > 0:
            remaining_deferral = max(0, SOLO_401K_LIMITS["employee_deferral"] - ext_result["total_401k"])
            s401k = calculate_solo_401k(business_income, b["se_deduction"], min(solo_401k_employee, remaining_deferral), employer_401k_percent, age, False)
            b["solo_401k_employee_contrib"] = s401k["employee_contrib"]
            b["solo_401k_employer_contrib"] = s401k["employer_contrib"]
            b["solo_401k_deduction"] = s401k["total_deduction"]

        if after_tax_401k > 0:
            pre_total = b["solo_401k_employee_contrib"] + b["solo_401k_employer_contrib"]
            b["after_tax_401k_contrib"] = min(after_tax_401k, max(0, SOLO_401K_LIMITS["total_limit"] - pre_total))

        if backdoor_roth > 0:
            b["backdoor_roth_contrib"] = min(backdoor_roth, IRA_LIMIT)
        if spouse_backdoor_roth > 0 and filing_status in ("mfj", "qw"):
            b["spouse_backdoor_roth_contrib"] = min(spouse_backdoor_roth, IRA_LIMIT)

        if se_health_insurance > 0:
            b["se_health_insurance_deduction"] = min(se_health_insurance, max(0, business_income - b["se_deduction"]))

        b["adjusted_gross_income"] = (
            business_income + ext_result["total_wages"] - ext_result["total_401k"]
            - b["se_deduction"] - b["se_health_insurance_deduction"]
            - b["solo_401k_deduction"] - b["hsa_deduction"]
        )

        taxable_before_qbid = max(0, b["adjusted_gross_income"] - standard_deduction)

        qbid = calculate_qbid(business_income, taxable_before_qbid, filing_status, is_sst, 0)
        b["qbid_deduction"] = qbid["deduction"]
        b["qbid_limited_by_sstb"] = qbid["limited_by_sstb"]
        b["qbid_limited_by_w2"] = qbid["limited_by_w2"]

        b["taxable_income"] = max(0, taxable_before_qbid - b["qbid_deduction"])
        b["total_deductions"] = (
            standard_deduction + b["se_deduction"] + b["se_health_insurance_deduction"]
            + b["qbid_deduction"] + b["solo_401k_deduction"] + b["hsa_deduction"]
        )

    else:
        # S-Corporation
        salary = min(reasonable_salary, business_income)
        b["salary"] = salary
        b["distributions"] = business_income - salary

        if salary > 0:
            other_medicare = external_medicare_income + effective_spouse_w2
            pr = calculate_payroll_tax(salary, filing_status, other_medicare, external_ss_wages)
            for k in ("employer_ss", "employee_ss", "employer_medicare", "employee_medicare", "additional_medicare_on_wages", "total_payroll_tax"):
                b[k] = pr[k]

        if (solo_401k_employee > 0 or employer_401k_percent > 0) and salary > 0:
            remaining_deferral = max(0, SOLO_401K_LIMITS["employee_deferral"] - ext_result["total_401k"])
            s401k = calculate_solo_401k(salary, 0, min(solo_401k_employee, remaining_deferral), employer_401k_percent, age, True)
            b["solo_401k_employee_contrib"] = s401k["employee_contrib"]
            b["solo_401k_employer_contrib"] = s401k["employer_contrib"]
            b["solo_401k_deduction"] = s401k["total_deduction"]

        if after_tax_401k > 0 and salary > 0:
            pre_total = b["solo_401k_employee_contrib"] + b["solo_401k_employer_contrib"]
            b["after_tax_401k_contrib"] = min(after_tax_401k, max(0, SOLO_401K_LIMITS["total_limit"] - pre_total))

        if backdoor_roth > 0:
            b["backdoor_roth_contrib"] = min(backdoor_roth, IRA_LIMIT)
        if spouse_backdoor_roth > 0 and filing_status in ("mfj", "qw"):
            b["spouse_backdoor_roth_contrib"] = min(spouse_backdoor_roth, IRA_LIMIT)

        b["scorp_health_insurance_deduction"] = scorp_health_insurance

        employer_payroll = b["employer_ss"] + b["employer_medicare"]
        adjusted_distributions = b["distributions"] - employer_payroll - b["solo_401k_employer_contrib"] - scorp_health_insurance

        # PTET
        if elect_ptet and has_ptet(state_code) and entity_type == "scorp":
            est_agi = salary + max(0, adjusted_distributions) - b["solo_401k_employee_contrib"] - b["hsa_deduction"] - spouse_result["employer_payroll"]
            est_taxable_before_qbid = max(0, est_agi - standard_deduction)
            est_total_w2 = salary + scorp_health_insurance + effective_spouse_w2
            est_qbid = calculate_qbid(max(0, adjusted_distributions), est_taxable_before_qbid, filing_status, is_sst, est_total_w2)
            ptet_nonconforming = is_qbid_nonconforming(state_code)
            state_std_ded = get_state_standard_deduction(state_code, filing_status, est_agi)
            est_state_taxable_before_qbid = max(0, est_agi - state_std_ded)
            est_state_taxable = (est_state_taxable_before_qbid if ptet_nonconforming
                                 else max(0, est_state_taxable_before_qbid - est_qbid["deduction"]))
            ptet_state_tax, _ = calculate_state_tax(est_state_taxable, state_code, filing_status)
            if ptet_state_tax > 0:
                b["ptet_tax"] = ptet_state_tax
                b["ptet_credit"] = ptet_state_tax
                adjusted_distributions -= ptet_state_tax

        entity_tax = calculate_scorp_entity_taxes(business_income, gross_revenue, state_code)
        b["scorp_entity_tax"] = entity_tax["entity_tax"]
        b["scorp_llc_fee"] = entity_tax["llc_fee"]
        if entity_tax["total"] > 0:
            adjusted_distributions -= entity_tax["total"]

        b["k1_income"] = max(0, adjusted_distributions)

        b["adjusted_gross_income"] = (
            salary + b["k1_income"] + ext_result["total_wages"] - ext_result["total_401k"]
            - b["solo_401k_employee_contrib"] - b["hsa_deduction"]
        )

        taxable_before_qbid = max(0, b["adjusted_gross_income"] - standard_deduction)

        total_w2_for_qbid = salary + scorp_health_insurance + effective_spouse_w2
        qbid = calculate_qbid(max(0, adjusted_distributions), taxable_before_qbid, filing_status, is_sst, total_w2_for_qbid)
        b["qbid_deduction"] = qbid["deduction"]
        b["qbid_limited_by_sstb"] = qbid["limited_by_sstb"]
        b["qbid_limited_by_w2"] = qbid["limited_by_w2"]

        b["taxable_income"] = max(0, taxable_before_qbid - b["qbid_deduction"])
        b["total_deductions"] = (
            standard_deduction + b["qbid_deduction"] + b["solo_401k_deduction"]
            + b["hsa_deduction"] + b["scorp_health_insurance_deduction"]
        )

    # Federal tax
    fed_tax, fed_details = calculate_federal_tax(b["taxable_income"], filing_status)
    b["federal_tax"] = fed_tax
    b["federal_tax_details"] = fed_details

    # California SDI
    if state_code == "CA" and entity_type == "scorp" and b["salary"] > 0:
        b["california_sdi"] = round(b["salary"] * 0.013)

    # State tax
    nonconforming = is_qbid_nonconforming(state_code)
    state_std_ded = get_state_standard_deduction(state_code, filing_status, b["adjusted_gross_income"])
    b["state_standard_deduction"] = state_std_ded
    state_agi_less_ded = b["adjusted_gross_income"] - state_std_ded
    state_taxable = max(0, state_agi_less_ded if nonconforming else state_agi_less_ded - b["qbid_deduction"])
    b["state_qbid_adjustment"] = b["qbid_deduction"] if nonconforming else 0
    b["state_taxable_income"] = state_taxable

    if entity_type == "sole_prop" or b["ptet_tax"] == 0:
        st_tax, st_details = calculate_state_tax(state_taxable, state_code, filing_status)
        b["state_tax"] = st_tax
        b["state_tax_details"] = st_details
    else:
        st_tax, st_details = calculate_state_tax(state_taxable, state_code, filing_status)
        b["state_tax_details"] = st_details
        b["state_tax"] = max(0, st_tax - b["ptet_credit"])

    if state_code == "UT" and b["state_tax"] > 0:
        utah_credit = round(standard_deduction * 0.06)
        b["utah_tax_credit"] = utah_credit
        b["state_tax"] = max(0, b["state_tax"] - utah_credit)

    if b["ptet_tax"] > 0:
        marginal = get_federal_marginal_rate(b["taxable_income"] + b["ptet_tax"], filing_status)
        b["ptet_net_benefit"] = round(b["ptet_tax"] * marginal)

    b["local_tax"] = calculate_local_tax(b["adjusted_gross_income"], city_code, entity_type)

    b["total_tax"] = (
        b["total_se_tax"] + b["total_payroll_tax"] + b["federal_tax"] + b["state_tax"]
        + b["local_tax"] + b["spouse_payroll_tax"] + b["ptet_tax"]
        + b["scorp_entity_tax"] + b["scorp_llc_fee"] + b["california_sdi"]
        + ext_result["total_payroll_tax"]
    )

    b["take_home"] = gross_revenue - business_expenses + b["external_w2_total"] - b["total_tax"]

    b["take_home_cash"] = (
        b["take_home"] - b["solo_401k_deduction"] - b["after_tax_401k_contrib"]
        - b["spouse_401k_deduction"] - b["spouse_after_tax_401k_contrib"]
        - b["external_w2_401k"] - b["external_w2_after_tax_401k"] - b["hsa_deduction"]
    )

    total_income = net_business_income + b["external_w2_total"]
    b["effective_rate"] = b["total_tax"] / total_income if total_income > 0 else 0

    return b


# =============================================================================
# STEP-BY-STEP PRINTOUT
# =============================================================================

def fmt(n):
    if isinstance(n, float) and n < 1:
        return f"{n:.1%}"
    return f"${n:,.0f}"


def print_results(b, inputs):
    entity = inputs.get("entity_type", "sole_prop")
    state = inputs.get("state_code", "CA")
    filing = inputs.get("filing_status", "single")

    print("=" * 60)
    print("  2026 TAX ESTIMATE")
    print("=" * 60)
    print(f"  Entity:  {entity.upper().replace('_', ' ')}")
    print(f"  Filing:  {filing.upper()}")
    print(f"  State:   {state}")
    if inputs.get("city_code"):
        print(f"  City:    {inputs['city_code']}")
    print(f"  Age:     {inputs.get('age', 40)}")
    print()

    print("--- INCOME ---")
    print(f"  Gross Revenue:       {fmt(b['gross_revenue'])}")
    print(f"  Business Expenses:   {fmt(b['business_expenses'])}")
    print(f"  Net Business Income: {fmt(b['net_business_income'])}")
    if b["external_w2_total"] > 0:
        print(f"  External W-2 Wages:  {fmt(b['external_w2_total'])}")
    print()

    if entity == "sole_prop":
        print("--- SELF-EMPLOYMENT TAX ---")
        print(f"  SE Base (92.35%):        {fmt(round(b['net_business_income'] * 0.9235))}")
        print(f"  Social Security Tax:     {fmt(b['social_security_tax'])}")
        print(f"  Medicare Tax:            {fmt(b['medicare_tax'])}")
        if b["additional_medicare_tax"] > 0:
            print(f"  Additional Medicare:     {fmt(b['additional_medicare_tax'])}")
        print(f"  Total SE Tax:            {fmt(b['total_se_tax'])}")
        print(f"  SE Deduction (50%):      {fmt(b['se_deduction'])}")
    else:
        print("--- S-CORP BREAKDOWN ---")
        print(f"  W-2 Salary:          {fmt(b['salary'])}")
        print(f"  Distributions:       {fmt(b['distributions'])}")
        print(f"  K-1 Income:          {fmt(b['k1_income'])}")
        print()
        print("--- PAYROLL TAX ---")
        print(f"  Employer SS:             {fmt(b['employer_ss'])}")
        print(f"  Employee SS:             {fmt(b['employee_ss'])}")
        print(f"  Employer Medicare:       {fmt(b['employer_medicare'])}")
        print(f"  Employee Medicare:       {fmt(b['employee_medicare'])}")
        if b["additional_medicare_on_wages"] > 0:
            print(f"  Additional Medicare:     {fmt(b['additional_medicare_on_wages'])}")
        print(f"  Total Payroll Tax:       {fmt(b['total_payroll_tax'])}")
        if b["scorp_entity_tax"] > 0 or b["scorp_llc_fee"] > 0:
            print()
            print("--- ENTITY TAXES ---")
            print(f"  S-Corp Entity Tax:   {fmt(b['scorp_entity_tax'])}")
            if b["scorp_llc_fee"] > 0:
                print(f"  LLC Fee:             {fmt(b['scorp_llc_fee'])}")
        if b["california_sdi"] > 0:
            print(f"  California SDI:      {fmt(b['california_sdi'])}")
    print()

    if b["solo_401k_deduction"] > 0:
        print("--- SOLO 401(k) ---")
        print(f"  Employee Deferral:   {fmt(b['solo_401k_employee_contrib'])}")
        print(f"  Employer Match:      {fmt(b['solo_401k_employer_contrib'])}")
        print(f"  Total Deduction:     {fmt(b['solo_401k_deduction'])}")
        if b["after_tax_401k_contrib"] > 0:
            print(f"  After-Tax (Mega):    {fmt(b['after_tax_401k_contrib'])}")
        print()

    if b["spouse_payroll_tax"] > 0:
        print("--- SPOUSE EMPLOYMENT ---")
        print(f"  Spouse W-2:          {fmt(inputs.get('spouse_w2', 0))}")
        print(f"  Employer Payroll:    {fmt(b['spouse_employer_payroll'])}")
        print(f"  Employee Payroll:    {fmt(b['spouse_employee_payroll'])}")
        if b["spouse_401k_deduction"] > 0:
            print(f"  Spouse 401(k):       {fmt(b['spouse_401k_deduction'])}")
        print()

    print("--- AGI & DEDUCTIONS ---")
    print(f"  Adjusted Gross Income:   {fmt(b['adjusted_gross_income'])}")
    print(f"  Standard Deduction:      {fmt(b['standard_deduction'])}")
    if b["se_deduction"] > 0:
        print(f"  SE Deduction:            {fmt(b['se_deduction'])}")
    if b["se_health_insurance_deduction"] > 0:
        print(f"  SE Health Insurance:     {fmt(b['se_health_insurance_deduction'])}")
    if b["scorp_health_insurance_deduction"] > 0:
        print(f"  S-Corp Health Ins:       {fmt(b['scorp_health_insurance_deduction'])}")
    if b["solo_401k_deduction"] > 0:
        print(f"  Solo 401(k) Deduction:   {fmt(b['solo_401k_deduction'])}")
    if b["hsa_deduction"] > 0:
        print(f"  HSA Deduction:           {fmt(b['hsa_deduction'])}")
    if b["qbid_deduction"] > 0:
        note = ""
        if b["qbid_limited_by_sstb"]:
            note = " (limited by SSTB)"
        elif b["qbid_limited_by_w2"]:
            note = " (limited by W-2 wages)"
        print(f"  QBID:                    {fmt(b['qbid_deduction'])}{note}")
    print(f"  Total Deductions:        {fmt(b['total_deductions'])}")
    print(f"  Taxable Income:          {fmt(b['taxable_income'])}")
    print()

    print("--- FEDERAL TAX ---")
    for d in b["federal_tax_details"]:
        pct = f"{d['rate']*100:.0f}%"
        print(f"  {pct:>5}  on {fmt(d['taxable_in_bracket']):>10} = {fmt(d['tax_in_bracket']):>9}")
    print(f"  {'Total':>27} = {fmt(b['federal_tax']):>9}")

    if b["ptet_tax"] > 0:
        print()
        print("--- PTET ---")
        print(f"  PTET Tax Paid:       {fmt(b['ptet_tax'])}")
        print(f"  PTET Credit:         {fmt(b['ptet_credit'])}")
        print(f"  Net Federal Benefit: {fmt(b['ptet_net_benefit'])}")

    if b["state_tax"] > 0 or b["state_tax_details"]:
        print()
        print(f"--- STATE TAX ({state}) ---")
        if b["state_standard_deduction"] > 0:
            print(f"  State Std Deduction: {fmt(b['state_standard_deduction'])}")
        if b["state_qbid_adjustment"] > 0:
            print(f"  QBID Add-Back:       {fmt(b['state_qbid_adjustment'])}")
        print(f"  State Taxable:       {fmt(b['state_taxable_income'])}")
        for d in b["state_tax_details"]:
            pct = f"{d['rate']*100:.2f}%"
            print(f"  {pct:>7}  on {fmt(d['taxable_in_bracket']):>10} = {fmt(d['tax_in_bracket']):>9}")
        if b.get("utah_tax_credit", 0) > 0:
            print(f"  Utah Tax Credit:     -{fmt(b['utah_tax_credit'])}")
        if b["ptet_credit"] > 0 and entity == "scorp":
            print(f"  Less PTET Credit:    -{fmt(b['ptet_credit'])}")
        print(f"  State Tax Due:       {fmt(b['state_tax'])}")

    if b["local_tax"] > 0:
        print()
        print(f"--- LOCAL TAX ---")
        print(f"  Local Tax:           {fmt(b['local_tax'])}")

    ext_payroll = sum(d["total_payroll_tax"] for d in b["external_w2_details"])
    if ext_payroll > 0:
        print()
        print("--- EXTERNAL W-2 PAYROLL ---")
        for d in b["external_w2_details"]:
            print(f"  {d['label']}: {fmt(d['wages'])} wages -> {fmt(d['total_payroll_tax'])} payroll tax")

    print()
    print("=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print(f"  Total Tax:           {fmt(b['total_tax'])}")
    print(f"  Take-Home:           {fmt(b['take_home'])}")
    print(f"  Spendable Cash:      {fmt(b['take_home_cash'])}")
    print(f"  Effective Rate:      {b['effective_rate']:.1%}")

    retirement = (
        b["solo_401k_deduction"] + b["after_tax_401k_contrib"] + b["backdoor_roth_contrib"]
        + b["spouse_401k_deduction"] + b["spouse_after_tax_401k_contrib"]
        + b["spouse_backdoor_roth_contrib"] + b["external_w2_401k"]
        + b["external_w2_after_tax_401k"] + b["hsa_deduction"]
    )
    if retirement > 0:
        print(f"  Retirement Savings:  {fmt(retirement)}")
    print("=" * 60)


# =============================================================================
# DEFAULT EXAMPLE
# =============================================================================

if __name__ == "__main__":
    inputs = {
        "gross_revenue": 300_000,
        "business_expenses": 50_000,
        "filing_status": "single",
        "state_code": "CA",
        "entity_type": "sole_prop",
        "age": 40,
        "solo_401k_employee": 24_500,
        "employer_401k_percent": 25,
        "hsa_contribution": 4_400,
        "backdoor_roth": 7_500,
    }

    result = calculate_taxes(inputs)
    print_results(result, inputs)
