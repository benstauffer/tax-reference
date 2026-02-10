---
lists:
  no_tax: [AK, FL, NV, NH, SD, TN, TX, WA, WY]
  ptet: [AL, AZ, AR, CA, CO, CT, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MS, MO, MT, NE, NJ, NM, NY, NC, OH, OK, OR, RI, SC, UT, WV, WI]
  qbid_nonconforming: [CA, DC, HI, MN, NJ, NY, OR, PA, SC, VT]
local:
  NYC: { name: "New York City", state: NY, rate: 0.03876 }
  PHL: { name: "Philadelphia", state: PA, rate: 0.0375 }
  SF:  { name: "San Francisco", state: CA, rate: 0.0038 }
ca_scorp_entity_tax:
  rate: 0.015
  minimum: 800
  llc_fee_brackets:
    - { min: 0, max: 250000, fee: 0 }
    - { min: 250000, max: 500000, fee: 900 }
    - { min: 500000, max: 1000000, fee: 2500 }
    - { min: 1000000, max: 5000000, fee: 6000 }
    - { min: 5000000, max: null, fee: 11790 }
federal_conformity_deductions: [CO, DC, ID, MO, MT, NM, SC]
---

# State Income Tax Overview (2026)

WA has 7% capital gains tax on gains >278K (+2.9% surcharge on 1M+).

QBID non-conforming states tax QBI at full state rate.

## PTET Notes

PTET expired: MN (12/31/2025). Pending extension: VA.

No S-Corp recognition: NYC, NH, TN, DC.

## S-Corp Entity Taxes

| Jurisdiction | Tax Name | Rate | Base | Minimum |
|--------------|----------|------|------|---------|
| NYC | General Corporation Tax | 8.85% | Net income | 25-5,000 |
| NH | Business Profits Tax | 7.5% | Net income | 0 |
| TN | Franchise & Excise Tax | 6.5% + 0.25% net worth | Net income | 100 |
| DC | Franchise Tax | 8.25% | Net income | 250 |

| State | Type | Rate | Minimum | Notes |
|-------|------|------|---------|-------|
| CA | Entity tax | 1.5% | 800 | Plus LLC fee |
| IL | Replacement tax | 1.5% | 0 | |
| NY | Fixed dollar min | — | 25-4,500 | Based on NY receipts |
| NJ | Minimum tax | — | 375-1,500 | Based on gross receipts |

---

## Data Source Legend

- **official_2026**: Official state DOR 2026 publication
- **2025_no_2026_update**: 2025 document still current
- **2025_unchanged**: Rates unchanged from prior years
- **2025_no_inflation_adj**: State does NOT inflation-adjust brackets
- **2025_rolling_pub**: Rolling publication - verify revision date

---
