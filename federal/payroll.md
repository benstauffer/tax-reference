---
payroll:
  ss_wage_base: 184500
  ss_rate: 0.124
  ss_max_tax: 22878
  ss_max_tax_per_side: 11439
  medicare_rate: 0.029
  additional_medicare_rate: 0.009
  se_taxable_multiplier: 0.9235
additional_medicare_thresholds:
  single: 200000
  mfj: 250000
  mfs: 125000
  hoh: 200000
  qw: 250000
futa:
  gross_rate: 0.06
  credit: 0.054
  effective_rate: 0.006
  wage_base: 7000
  max_per_employee: 42
nanny_tax:
  fica_threshold: 3000
  futa_threshold: 1000
---

# Payroll Tax (2026)

Sources: SSA.gov, IRC §3101(b), IRC §1401, IRC §164(f)

## Additional Medicare Tax
- Not indexed (unchanged since 2013)
- CRITICAL: 0.9% additional Medicare is NOT deductible per IRC §164(f)

## Self-Employment Tax Calculation

1. SE Tax Base = Net SE Income × 0.9235
2. Social Security Tax = min(SE Tax Base, 184,500) × 12.4%
3. Medicare Tax = SE Tax Base × 2.9%
4. Regular SE Tax = Social Security Tax + Medicare Tax
5. Additional Medicare Tax = max(0, SE Tax Base - threshold) × 0.9%
6. Total SE Tax = Regular SE Tax + Additional Medicare Tax
7. **SE Tax Deduction = Regular SE Tax × 50%** (excludes Additional Medicare Tax!)

## FUTA
Credit reduction states (2025 wages): California, US Virgin Islands. 2026: TBD November 10, 2026.

## Nanny Tax
FICA threshold increased from 2,800 in 2025.
