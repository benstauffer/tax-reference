---
niit:
  rate: 0.038
  indexed: false
  thresholds:
    single: 200000
    mfj: 250000
    mfs: 125000
    hoh: 200000
    qw: 250000
qbid:
  rate: 0.20
  w2_wage_limit: 0.50
  w2_ubia_wage_pct: 0.25
  w2_ubia_ubia_pct: 0.025
  optimal_w2_ratio: 0.2857
  single:
    full_deduction: 201750
    phaseout_range: 75000
    phaseout_complete: 276750
  mfj:
    full_deduction: 403500
    phaseout_range: 150000
    phaseout_complete: 553500
salt_cap:
  limit: 40400
  limit_mfs: 20200
  floor: 10000
  floor_mfs: 5000
  phasedown_rate: 0.30
  phasedown_begins: 500500
  phasedown_begins_mfs: 250250
  phasedown_complete: 601833
  phasedown_complete_mfs: 300917
  annual_adjustment: 1.01
  expiration: "2029-12-31"
  reversion_amount: 10000
amt:
  exemption:
    single: 90100
    mfj: 140200
    mfs: 70100
  phaseout_begins:
    single: 500000
    mfj: 1000000
  threshold_28pct: 244500
other:
  kiddie_tax_threshold: 2700
  foreign_earned_income_exclusion: 132900
  educator_expense_deduction: 350
  adoption_credit_max: 17670
  student_loan_interest_max: 2500
---

# Key Thresholds (2026)


## NIIT
Not indexed (unchanged since 2013). 3.8% on lesser of: (1) net investment income, or (2) MAGI exceeding threshold.

**Applies to:** Interest, dividends, capital gains, rental income, royalties, passive income, non-qualified annuities

**Excludes:** Wages, SE income, active business income, retirement distributions, tax-exempt interest, veterans benefits, Social Security

**Planning:**
- Cannot be reduced by capital losses below zero
- Passive activity losses can reduce NII
- S-Corp distributions generally not NII if materially participating
- Rental income usually NII unless real estate professional

## QBID

**W-2 wage limitations (above threshold):**
- Option 1: 50% of W-2 wages
- Option 2: 25% of W-2 wages + 2.5% of UBIA

**SSTB (Specified Service Trades):**
- Below threshold: full deduction
- In phaseout: proportional reduction
- Above phaseout: NO deduction

**SSTB types:** Health, law, accounting, actuarial, performing arts, consulting, athletics, financial services, brokerage, investment management, trading, any trade where principal asset is reputation/skill

**SSTB exclusions:** Architecture, engineering

**State conformity:** Most states conform. Does NOT conform: CA, NJ, PA, HI, MN, OR, VT, NY, DC, SC. Partial: GA.

## SALT Cap
Cap reduced by 30% of MAGI exceeding threshold; cannot fall below floor.

## Kiddie Tax
2,700 unearned income threshold.
