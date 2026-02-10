---
name: tax
description: Calculates 2026 US federal and state taxes for solopreneurs. Use when computing tax liability, planning retirement contributions, comparing state tax rates, determining self-employment tax, or answering questions about brackets, deductions, QBID, NIIT, SALT, or PTET.
allowed-tools:
  - Read
---

# 2026 US Tax Reference

Quick reference for solopreneurs. TCJA extended via OBBBA (July 2025).

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

## Routing Table

Load ONLY the file(s) needed to answer the question. For multi-topic questions, load each relevant file.

### Federal Topics
| Topic | File |
|-------|------|
| Brackets, standard deduction, senior deduction, capital gains, LTCG | [federal/income-tax.md](federal/income-tax.md) |
| SS, Medicare, SE tax, FUTA, nanny tax | [federal/payroll.md](federal/payroll.md) |
| 401(k), IRA, Roth, HSA, SEP, SIMPLE, FSA, defined benefit, savers credit | [federal/retirement.md](federal/retirement.md) |
| NIIT, QBID, SALT cap, AMT, kiddie tax, FEIE, adoption credit, student loan interest | [federal/thresholds.md](federal/thresholds.md) |
| Section 179, bonus depreciation, MACRS | [federal/depreciation.md](federal/depreciation.md) |
| Estate tax, gift tax, GST, portability | [federal/estate-gift.md](federal/estate-gift.md) |

### State Topics
| Topic | File |
|-------|------|
| No tax / flat tax / QBID / PTET lists, S-Corp entity taxes | [state/overview.md](state/overview.md) |
| AK, FL, NV, NH, SD, TN, TX, WA, WY | [state/no-income-tax.md](state/no-income-tax.md) |
| AZ, CO, GA, ID, IL, IN, IA, KY, LA, MI, MO, MS, NC, OH, PA, UT | [state/flat-tax.md](state/flat-tax.md) |
| AL, AR, CA, CT, DC, DE, HI, KS, MA, ME, MD, MN | [state/graduated-AL-MN.md](state/graduated-AL-MN.md) |
| MT, NE, NJ, NM, NY, ND, OK, OR, RI, SC, VT, VA, WV, WI | [state/graduated-MT-WI.md](state/graduated-MT-WI.md) |
| PTET rates, credit types, election timing | [state/ptet.md](state/ptet.md) |

### Calculations
| Topic | File |
|-------|------|
| Run tax estimate, step-by-step calculation, verify math, Python calculator | [estimate.py](estimate.py) |

## Filing Status Codes

| Code | Meaning |
|------|---------|
| single | Single filer |
| mfj | Married Filing Jointly |
| mfs | Married Filing Separately |
| hoh | Head of Household |
| qw | Qualifying Widow(er) |

## Data Conventions

- Rates shown as "10%" in tables, use 0.10 for calculations
- Dollar amounts as integers, no $ in data columns
- Unbounded maximums shown as "—"
