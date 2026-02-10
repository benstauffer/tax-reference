---
name: tax
description: Calculates 2026 US federal and state taxes for solopreneurs. Use when computing tax liability, planning retirement contributions, comparing state tax rates, determining self-employment tax, or answering questions about brackets, deductions, QBID, NIIT, SALT, or PTET.
---

# 2026 US Tax Reference

All tax data is in [reference/tax.md](reference/tax.md) (YAML frontmatter + notes). For step-by-step calculations, run [scripts/estimate.py](scripts/estimate.py) (requires `pyyaml`).

## Quick Reference

| Item | Single | MFJ |
|------|--------|-----|
| Standard Deduction | 16,100 | 32,200 |
| Top Bracket Starts | 640,601 | 768,701 |
| LTCG 0% Up To | 49,450 | 98,900 |
| SS Wage Base | 184,500 | 184,500 |
| 401(k) Limit | 24,500 | 24,500 |
| SALT Cap | 40,400 | 40,400 |
| NIIT Threshold | 200,000 | 250,000 |
| QBID Full Below | 201,750 | 403,500 |

## Key Numbers

- **SS**: 184,500 wage base, 12.4% SE rate, max 22,878
- **Medicare**: 2.9% SE (no cap), +0.9% above 200K/250K (NOT deductible)
- **401(k)**: 24,500 (+8,000 catch-up 50+, +11,250 super 60-63)
- **IRA**: 7,500 (+1,100 catch-up 50+)
- **HSA**: 4,400 individual / 8,750 family (+1,000 catch-up 55+)
- **SEP-IRA**: 25% of comp, max 72,000
- **Section 179**: 1,220,000 (phases out at 3,050,000)
- **Bonus depreciation**: 100% (restored via OBBBA)
- **Estate exemption**: 15M | **Gift exclusion**: 19,000

## Data Location

All brackets, thresholds, and state data are in the YAML frontmatter of [reference/tax.md](reference/tax.md). Notes and state-specific commentary follow after the frontmatter. Read reference/tax.md to answer any question about specific numbers, brackets, or rules.

For calculations, run [scripts/estimate.py](scripts/estimate.py) with a Python interpreter (`pip install pyyaml`).

## Filing Status Codes

| Code | Meaning |
|------|---------|
| single | Single filer |
| mfj | Married Filing Jointly |
| mfs | Married Filing Separately |
| hoh | Head of Household |
| qw | Qualifying Widow(er) |

## YAML Frontmatter Keys

| Key | Contains |
|-----|----------|
| `brackets`, `standard_deductions`, `capital_gains` | Federal income tax |
| `payroll`, `additional_medicare_thresholds`, `futa` | Payroll & SE tax |
| `niit`, `qbid`, `salt_cap`, `amt` | Key thresholds |
| `solo_401k`, `ira_limit`, `hsa`, `sep_ira`, `fsa` | Retirement & savings |
| `section_179`, `bonus_depreciation`, `macrs` | Depreciation |
| `estate_exemption`, `gift_exemption`, `annual_exclusion` | Estate & gift |
| `state_no_tax`, `state_flat`, `state_graduated_*` | State brackets |
| `state_flat_standard_deductions`, `state_graduated_*_standard_deductions` | State deductions |
| `ptet`, `ptet_expired` | PTET rates & credits |
| `state_lists`, `local`, `ca_scorp_entity_tax` | State overview & entity taxes |
