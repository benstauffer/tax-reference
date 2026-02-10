---
states:
  MT:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 47500, rate: 0.047 }
        - { min: 47500, max: null, rate: 0.0565 }
      mfj:
        - { min: 0, max: 95000, rate: 0.047 }
        - { min: 95000, max: null, rate: 0.0565 }
      mfs:
        - { min: 0, max: 47500, rate: 0.047 }
        - { min: 47500, max: null, rate: 0.0565 }
      hoh:
        - { min: 0, max: 71250, rate: 0.047 }
        - { min: 71250, max: null, rate: 0.0565 }
  NE:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 2400, rate: 0.0246 }
        - { min: 2400, max: 18000, rate: 0.0351 }
        - { min: 18000, max: null, rate: 0.0455 }
      mfj:
        - { min: 0, max: 4800, rate: 0.0246 }
        - { min: 4800, max: 36000, rate: 0.0351 }
        - { min: 36000, max: null, rate: 0.0455 }
      mfs:
        - { min: 0, max: 2400, rate: 0.0246 }
        - { min: 2400, max: 18000, rate: 0.0351 }
        - { min: 18000, max: null, rate: 0.0455 }
      hoh:
        - { min: 0, max: 3840, rate: 0.0246 }
        - { min: 3840, max: 28800, rate: 0.0351 }
        - { min: 28800, max: null, rate: 0.0455 }
  NJ:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 20000, rate: 0.014 }
        - { min: 20000, max: 35000, rate: 0.0175 }
        - { min: 35000, max: 40000, rate: 0.035 }
        - { min: 40000, max: 75000, rate: 0.05525 }
        - { min: 75000, max: 500000, rate: 0.0637 }
        - { min: 500000, max: 1000000, rate: 0.0897 }
        - { min: 1000000, max: null, rate: 0.1075 }
      mfj:
        - { min: 0, max: 20000, rate: 0.014 }
        - { min: 20000, max: 50000, rate: 0.0175 }
        - { min: 50000, max: 70000, rate: 0.0245 }
        - { min: 70000, max: 80000, rate: 0.035 }
        - { min: 80000, max: 150000, rate: 0.05525 }
        - { min: 150000, max: 500000, rate: 0.0637 }
        - { min: 500000, max: 1000000, rate: 0.0897 }
        - { min: 1000000, max: null, rate: 0.1075 }
      mfs:
        - { min: 0, max: 20000, rate: 0.014 }
        - { min: 20000, max: 35000, rate: 0.0175 }
        - { min: 35000, max: 40000, rate: 0.035 }
        - { min: 40000, max: 75000, rate: 0.05525 }
        - { min: 75000, max: 500000, rate: 0.0637 }
        - { min: 500000, max: 1000000, rate: 0.0897 }
        - { min: 1000000, max: null, rate: 0.1075 }
      hoh:
        - { min: 0, max: 20000, rate: 0.014 }
        - { min: 20000, max: 50000, rate: 0.0175 }
        - { min: 50000, max: 70000, rate: 0.0245 }
        - { min: 70000, max: 80000, rate: 0.035 }
        - { min: 80000, max: 150000, rate: 0.05525 }
        - { min: 150000, max: 500000, rate: 0.0637 }
        - { min: 500000, max: 1000000, rate: 0.0897 }
        - { min: 1000000, max: null, rate: 0.1075 }
  NM:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 5500, rate: 0.015 }
        - { min: 5500, max: 16500, rate: 0.032 }
        - { min: 16500, max: 33500, rate: 0.043 }
        - { min: 33500, max: 66500, rate: 0.047 }
        - { min: 66500, max: 210000, rate: 0.049 }
        - { min: 210000, max: null, rate: 0.059 }
      mfj:
        - { min: 0, max: 8000, rate: 0.015 }
        - { min: 8000, max: 25000, rate: 0.032 }
        - { min: 25000, max: 50000, rate: 0.043 }
        - { min: 50000, max: 100000, rate: 0.047 }
        - { min: 100000, max: 315000, rate: 0.049 }
        - { min: 315000, max: null, rate: 0.059 }
      mfs:
        - { min: 0, max: 4000, rate: 0.015 }
        - { min: 4000, max: 12500, rate: 0.032 }
        - { min: 12500, max: 25000, rate: 0.043 }
        - { min: 25000, max: 50000, rate: 0.047 }
        - { min: 50000, max: 157500, rate: 0.049 }
        - { min: 157500, max: null, rate: 0.059 }
      hoh:
        - { min: 0, max: 8000, rate: 0.015 }
        - { min: 8000, max: 25000, rate: 0.032 }
        - { min: 25000, max: 50000, rate: 0.043 }
        - { min: 50000, max: 100000, rate: 0.047 }
        - { min: 100000, max: 315000, rate: 0.049 }
        - { min: 315000, max: null, rate: 0.059 }
  NY:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 8500, rate: 0.04 }
        - { min: 8500, max: 11700, rate: 0.045 }
        - { min: 11700, max: 13900, rate: 0.0525 }
        - { min: 13900, max: 80650, rate: 0.055 }
        - { min: 80650, max: 215400, rate: 0.06 }
        - { min: 215400, max: 1077550, rate: 0.0685 }
        - { min: 1077550, max: 5000000, rate: 0.0965 }
        - { min: 5000000, max: 25000000, rate: 0.103 }
        - { min: 25000000, max: null, rate: 0.109 }
      mfj:
        - { min: 0, max: 17150, rate: 0.04 }
        - { min: 17150, max: 23600, rate: 0.045 }
        - { min: 23600, max: 27900, rate: 0.0525 }
        - { min: 27900, max: 161550, rate: 0.055 }
        - { min: 161550, max: 323200, rate: 0.06 }
        - { min: 323200, max: 2155350, rate: 0.0685 }
        - { min: 2155350, max: 5000000, rate: 0.0965 }
        - { min: 5000000, max: 25000000, rate: 0.103 }
        - { min: 25000000, max: null, rate: 0.109 }
      mfs:
        - { min: 0, max: 8500, rate: 0.04 }
        - { min: 8500, max: 11700, rate: 0.045 }
        - { min: 11700, max: 13900, rate: 0.0525 }
        - { min: 13900, max: 80650, rate: 0.055 }
        - { min: 80650, max: 215400, rate: 0.06 }
        - { min: 215400, max: 1077550, rate: 0.0685 }
        - { min: 1077550, max: 5000000, rate: 0.0965 }
        - { min: 5000000, max: 25000000, rate: 0.103 }
        - { min: 25000000, max: null, rate: 0.109 }
      hoh:
        - { min: 0, max: 12800, rate: 0.04 }
        - { min: 12800, max: 17650, rate: 0.045 }
        - { min: 17650, max: 20900, rate: 0.0525 }
        - { min: 20900, max: 107650, rate: 0.055 }
        - { min: 107650, max: 269300, rate: 0.06 }
        - { min: 269300, max: 1616450, rate: 0.0685 }
        - { min: 1616450, max: 5000000, rate: 0.0965 }
        - { min: 5000000, max: 25000000, rate: 0.103 }
        - { min: 25000000, max: null, rate: 0.109 }
  ND:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 48475, rate: 0.0 }
        - { min: 48475, max: 244825, rate: 0.0195 }
        - { min: 244825, max: null, rate: 0.025 }
      mfj:
        - { min: 0, max: 80975, rate: 0.0 }
        - { min: 80975, max: 298075, rate: 0.0195 }
        - { min: 298075, max: null, rate: 0.025 }
      mfs:
        - { min: 0, max: 40475, rate: 0.0 }
        - { min: 40475, max: 149025, rate: 0.0195 }
        - { min: 149025, max: null, rate: 0.025 }
      hoh:
        - { min: 0, max: 64950, rate: 0.0 }
        - { min: 64950, max: 271450, rate: 0.0195 }
        - { min: 271450, max: null, rate: 0.025 }
  OK:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 1000, rate: 0.0025 }
        - { min: 1000, max: 7200, rate: 0.0375 }
        - { min: 7200, max: null, rate: 0.045 }
      mfj:
        - { min: 0, max: 2000, rate: 0.0025 }
        - { min: 2000, max: 14400, rate: 0.0375 }
        - { min: 14400, max: null, rate: 0.045 }
      mfs:
        - { min: 0, max: 1000, rate: 0.0025 }
        - { min: 1000, max: 7200, rate: 0.0375 }
        - { min: 7200, max: null, rate: 0.045 }
      hoh:
        - { min: 0, max: 2000, rate: 0.0025 }
        - { min: 2000, max: 14400, rate: 0.0375 }
        - { min: 14400, max: null, rate: 0.045 }
  OR:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 4550, rate: 0.0475 }
        - { min: 4550, max: 11400, rate: 0.0675 }
        - { min: 11400, max: 125000, rate: 0.0875 }
        - { min: 125000, max: null, rate: 0.099 }
      mfj:
        - { min: 0, max: 9100, rate: 0.0475 }
        - { min: 9100, max: 22800, rate: 0.0675 }
        - { min: 22800, max: 250000, rate: 0.0875 }
        - { min: 250000, max: null, rate: 0.099 }
      mfs:
        - { min: 0, max: 4550, rate: 0.0475 }
        - { min: 4550, max: 11400, rate: 0.0675 }
        - { min: 11400, max: 125000, rate: 0.0875 }
        - { min: 125000, max: null, rate: 0.099 }
      hoh:
        - { min: 0, max: 9100, rate: 0.0475 }
        - { min: 9100, max: 22800, rate: 0.0675 }
        - { min: 22800, max: 250000, rate: 0.0875 }
        - { min: 250000, max: null, rate: 0.099 }
  RI:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 79900, rate: 0.0375 }
        - { min: 79900, max: 181650, rate: 0.0475 }
        - { min: 181650, max: null, rate: 0.0599 }
      mfj:
        - { min: 0, max: 79900, rate: 0.0375 }
        - { min: 79900, max: 181650, rate: 0.0475 }
        - { min: 181650, max: null, rate: 0.0599 }
      mfs:
        - { min: 0, max: 79900, rate: 0.0375 }
        - { min: 79900, max: 181650, rate: 0.0475 }
        - { min: 181650, max: null, rate: 0.0599 }
      hoh:
        - { min: 0, max: 79900, rate: 0.0375 }
        - { min: 79900, max: 181650, rate: 0.0475 }
        - { min: 181650, max: null, rate: 0.0599 }
  SC:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 3460, rate: 0.0 }
        - { min: 3460, max: 17330, rate: 0.03 }
        - { min: 17330, max: null, rate: 0.06 }
      mfj:
        - { min: 0, max: 3460, rate: 0.0 }
        - { min: 3460, max: 17330, rate: 0.03 }
        - { min: 17330, max: null, rate: 0.06 }
      mfs:
        - { min: 0, max: 3460, rate: 0.0 }
        - { min: 3460, max: 17330, rate: 0.03 }
        - { min: 17330, max: null, rate: 0.06 }
      hoh:
        - { min: 0, max: 3460, rate: 0.0 }
        - { min: 3460, max: 17330, rate: 0.03 }
        - { min: 17330, max: null, rate: 0.06 }
  VT:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 47600, rate: 0.0335 }
        - { min: 47600, max: 115350, rate: 0.054 }
        - { min: 115350, max: 200200, rate: 0.066 }
        - { min: 200200, max: 254400, rate: 0.076 }
        - { min: 254400, max: null, rate: 0.0875 }
      mfj:
        - { min: 0, max: 79300, rate: 0.0335 }
        - { min: 79300, max: 192250, rate: 0.054 }
        - { min: 192250, max: 333650, rate: 0.066 }
        - { min: 333650, max: 424000, rate: 0.076 }
        - { min: 424000, max: null, rate: 0.0875 }
      mfs:
        - { min: 0, max: 47600, rate: 0.0335 }
        - { min: 47600, max: 115350, rate: 0.054 }
        - { min: 115350, max: 200200, rate: 0.066 }
        - { min: 200200, max: 254400, rate: 0.076 }
        - { min: 254400, max: null, rate: 0.0875 }
      hoh:
        - { min: 0, max: 79300, rate: 0.0335 }
        - { min: 79300, max: 192250, rate: 0.054 }
        - { min: 192250, max: 333650, rate: 0.066 }
        - { min: 333650, max: 424000, rate: 0.076 }
        - { min: 424000, max: null, rate: 0.0875 }
  VA:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 3000, rate: 0.02 }
        - { min: 3000, max: 5000, rate: 0.03 }
        - { min: 5000, max: 17000, rate: 0.05 }
        - { min: 17000, max: null, rate: 0.0575 }
      mfj:
        - { min: 0, max: 3000, rate: 0.02 }
        - { min: 3000, max: 5000, rate: 0.03 }
        - { min: 5000, max: 17000, rate: 0.05 }
        - { min: 17000, max: null, rate: 0.0575 }
      mfs:
        - { min: 0, max: 3000, rate: 0.02 }
        - { min: 3000, max: 5000, rate: 0.03 }
        - { min: 5000, max: 17000, rate: 0.05 }
        - { min: 17000, max: null, rate: 0.0575 }
      hoh:
        - { min: 0, max: 3000, rate: 0.02 }
        - { min: 3000, max: 5000, rate: 0.03 }
        - { min: 5000, max: 17000, rate: 0.05 }
        - { min: 17000, max: null, rate: 0.0575 }
  WV:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 10000, rate: 0.0236 }
        - { min: 10000, max: 25000, rate: 0.0315 }
        - { min: 25000, max: 40000, rate: 0.0354 }
        - { min: 40000, max: 60000, rate: 0.0472 }
        - { min: 60000, max: null, rate: 0.0512 }
      mfj:
        - { min: 0, max: 10000, rate: 0.0236 }
        - { min: 10000, max: 25000, rate: 0.0315 }
        - { min: 25000, max: 40000, rate: 0.0354 }
        - { min: 40000, max: 60000, rate: 0.0472 }
        - { min: 60000, max: null, rate: 0.0512 }
      mfs:
        - { min: 0, max: 5000, rate: 0.0236 }
        - { min: 5000, max: 12500, rate: 0.0315 }
        - { min: 12500, max: 20000, rate: 0.0354 }
        - { min: 20000, max: 30000, rate: 0.0472 }
        - { min: 30000, max: null, rate: 0.0512 }
      hoh:
        - { min: 0, max: 10000, rate: 0.0236 }
        - { min: 10000, max: 25000, rate: 0.0315 }
        - { min: 25000, max: 40000, rate: 0.0354 }
        - { min: 40000, max: 60000, rate: 0.0472 }
        - { min: 60000, max: null, rate: 0.0512 }
  WI:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 14320, rate: 0.035 }
        - { min: 14320, max: 28640, rate: 0.044 }
        - { min: 28640, max: 315310, rate: 0.053 }
        - { min: 315310, max: null, rate: 0.0765 }
      mfj:
        - { min: 0, max: 19090, rate: 0.035 }
        - { min: 19090, max: 38190, rate: 0.044 }
        - { min: 38190, max: 420420, rate: 0.053 }
        - { min: 420420, max: null, rate: 0.0765 }
      mfs:
        - { min: 0, max: 14320, rate: 0.035 }
        - { min: 14320, max: 28640, rate: 0.044 }
        - { min: 28640, max: 315310, rate: 0.053 }
        - { min: 315310, max: null, rate: 0.0765 }
      hoh:
        - { min: 0, max: 14320, rate: 0.035 }
        - { min: 14320, max: 28640, rate: 0.044 }
        - { min: 28640, max: 315310, rate: 0.053 }
        - { min: 315310, max: null, rate: 0.0765 }
standard_deductions:
  NE: { single: 8600, mfj: 17200, mfs: 8600, hoh: 12900 }
  NY: { single: 8000, mfj: 16050, mfs: 8000, hoh: 11200 }
  ND: { single: 15750, mfj: 31500, mfs: 15750, hoh: 23625 }
  OK: { single: 6350, mfj: 12700, mfs: 6350, hoh: 9350 }
  OR: { single: 2910, mfj: 5820, mfs: 2835, hoh: 5820 }
  RI: { single: 10900, mfj: 21800, mfs: 10900, hoh: 16350 }
  VA: { single: 8750, mfj: 17500, mfs: 8750, hoh: 8750 }
  VT: { single: 14600, mfj: 29200, mfs: 14600, hoh: 29200 }
  WV: { single: 2000, mfj: 4000, mfs: 2000, hoh: 2000 }
  WI: { single: 12760, mfj: 23620, mfs: 12760, hoh: 17840 }
---

# Graduated Tax States: MT–WI (2026)

## Montana
**Source:** [MT DOR](https://revenuefiles.mt.gov/files/Forms/Publication-1/Publication-1-2026.pdf) | **Data:** official_2026

Top rate 5.65%. Standard deduction: uses federal amounts. Capital gains: preferential (max 4.1%).

HB 337: Top rate 5.65%, lower bracket expanded to 47,500 for 2026. PTET: 5.65% rate, nonrefundable credit.

---

## Nebraska
**Source:** [NE DOR](https://revenue.nebraska.gov/sites/default/files/doc/business/Cir_En_2025/2026cir_en_whole.pdf) | **Data:** official_2026

Top rate 4.55%. 2026 rates: 2.46%/3.51%/4.55% per LB754 phased reduction. Additional for age 65+/blind.

PTET: 4.55% rate, refundable credit.

---

## New Jersey
**Source:** [NJ Treasury](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf) | **Data:** 2025_no_inflation_adj

Top rate 10.75%. NJ does NOT index brackets for inflation. No standard deduction (uses personal exemptions).

Personal exemption: 1,000 per person | Additional 65+/blind 1,000. Capital gains: ordinary income. QBID: does NOT conform.

S-Corp minimum tax: 375 (0-100K receipts), 750 (100K-250K), 1,000 (250K-500K), 1,250 (500K-1M), 1,500 (1M+).

PTET: 5.675-10.9% rate, refundable credit (top rate 10.9% not 10.75%).

---

## New Mexico
**Source:** [NM TRD](https://www.tax.newmexico.gov/businesses/wp-content/uploads/sites/4/2022/12/FYI-104_2025.pdf) | **Data:** 2025_no_2026_update

Top rate 5.9%. Standard deduction: uses federal amounts. 6 brackets, 1.5%-5.9% per HB 252 (2024).

PTET: 5.9% rate, refundable credit.

---

## New York
**Source:** [NY DTF](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf) | **Data:** official_2026

Top rate 10.9%. Capital gains: ordinary income. QBID: does NOT conform.

2026 includes 0.1% reduction in bottom 5 brackets. High-income surcharge extended through 2032.

NYC additional: 3.078%-3.876% for residents. S-corps taxed as C-corps at 8.85%.

S-Corp fixed dollar minimum (by NY receipts): 25 (0-100K), 50 (100K-250K), 175 (250K-500K), 300 (500K-1M), 1,000 (1M-5M), 3,000 (5M-25M), 4,500 (25M+).

PTET: 6.85-10.9% rate, refundable credit (election by March 15).

---

## North Dakota
**Source:** [ND Tax](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) | **Data:** official_2026

Top rate 2.5%. Standard deduction: uses federal amounts. Capital gains: 40% exclusion.

---

## Oklahoma
**Source:** [OK Tax](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf) | **Data:** official_2026

Top rate 4.5%. Consolidated to 3 brackets per HB 2764, top rate reduced from 4.75%. Trigger mechanism may phase out income tax entirely.

PTET: 4.5% rate, refundable credit.

---

## Oregon
**Source:** [OR DOR](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf) | **Data:** official_2026

Top rate 9.9%. Capital gains: ordinary income. QBID: does NOT conform.

Local tax: Portland Metro adds 1% supportive housing tax (>200K) + 1.5-3% Multnomah Co preschool tax on high earners.

CAT: 250 + 0.57% on commercial activity over 1M (after 35% subtraction).

2026 inflation-adjusted amounts. Brackets vary by # of exemptions. PTET: 9% rate, refundable credit.

---

## Rhode Island
**Source:** [RI Tax](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/2026%20Withholding%20Tax%20Booklet_d.pdf) | **Data:** official_2026

Top rate 5.99%. Same brackets for all filing statuses. Personal exemption: 5,100.

Standard deduction phases out for MAGI >254,250, reaching 0 at 283,250+. Surtax bills (H5473/S0329) died in committee.

PTET: 5.99% rate, refundable credit.

---

## South Carolina
**Source:** [SC DOR](https://dor.sc.gov/sites/dor/files/forms/WH1603_2026.pdf) | **Data:** official_2026

Top rate 6.0%. Same brackets for all filing statuses. Standard deduction: uses federal amounts. QBID: does NOT conform.

Top rate reduced from 6.2% for 2026. Brackets inflation-adjusted. PTET: 6.0% rate, refundable credit.

---

## Vermont
**Source:** [VT Tax](https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf) | **Data:** official_2026

Top rate 8.75%. QBID: does NOT conform. MFJ thresholds <2x Single (marriage penalty).

---

## Virginia
**Source:** [VA Tax](https://www.tax.virginia.gov/sites/default/files/taxforms/withholding/any/employer-withholding-tables-july-2025-and-later-any.pdf) | **Data:** official_2026

Top rate 5.75%. Same brackets for all filing statuses. Personal exemption: 930 per person | Additional 65+/blind 800.

HB 1754 (7% on >600K) proposed but not yet confirmed enacted. PTET: 5.75% rate, refundable credit (extended to Jan 1, 2027 - verify status).

---

## West Virginia
**Source:** [WV Tax](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) | **Data:** 2025_rates_pending_2026

Top rate 5.12%. MFS brackets are half of single/MFJ/HOH.

Social Security fully exempt from WV income tax starting 2026. Rates reduced per SB 2033. 2026 rates TBD per WV Code 11-21-4h.

PTET: 4.82% rate, refundable credit.

---

## Wisconsin
**Source:** [WI DOR](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf) | **Data:** official_2026

Top rate 7.65%. MFJ thresholds ~1.33x Single (not 2x), creating some marriage penalty.

Standard deduction phaseout: reduces by 12% of income above threshold (Single 16,390, MFJ 23,620).

PTET: 7.65% rate, refundable credit.
