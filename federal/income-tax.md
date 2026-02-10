---
brackets:
  single:
    - { min: 0, max: 12400, rate: 0.10 }
    - { min: 12400, max: 50400, rate: 0.12 }
    - { min: 50400, max: 105700, rate: 0.22 }
    - { min: 105700, max: 201775, rate: 0.24 }
    - { min: 201775, max: 256225, rate: 0.32 }
    - { min: 256225, max: 640600, rate: 0.35 }
    - { min: 640600, max: null, rate: 0.37 }
  mfj:
    - { min: 0, max: 24800, rate: 0.10 }
    - { min: 24800, max: 100800, rate: 0.12 }
    - { min: 100800, max: 211400, rate: 0.22 }
    - { min: 211400, max: 403550, rate: 0.24 }
    - { min: 403550, max: 512450, rate: 0.32 }
    - { min: 512450, max: 768700, rate: 0.35 }
    - { min: 768700, max: null, rate: 0.37 }
  mfs:
    - { min: 0, max: 12400, rate: 0.10 }
    - { min: 12400, max: 50400, rate: 0.12 }
    - { min: 50400, max: 105700, rate: 0.22 }
    - { min: 105700, max: 201775, rate: 0.24 }
    - { min: 201775, max: 256225, rate: 0.32 }
    - { min: 256225, max: 384350, rate: 0.35 }
    - { min: 384350, max: null, rate: 0.37 }
  hoh:
    - { min: 0, max: 17700, rate: 0.10 }
    - { min: 17700, max: 67450, rate: 0.12 }
    - { min: 67450, max: 105700, rate: 0.22 }
    - { min: 105700, max: 201775, rate: 0.24 }
    - { min: 201775, max: 256200, rate: 0.32 }
    - { min: 256200, max: 640600, rate: 0.35 }
    - { min: 640600, max: null, rate: 0.37 }
standard_deductions:
  single: 16100
  mfj: 32200
  mfs: 16100
  hoh: 24150
  qw: 32200
additional_standard_deduction:
  single_hoh: 2050   # per condition (65+ or blind)
  mfj_mfs: 1650      # per person per condition
personal_exemption: 0
senior_deduction:
  amount: 6000
  amount_mfj_both_65: 12000
  phaseout_begins: { single: 75000, mfj: 150000 }
  phaseout_complete: { single: 175000, mfj: 250000 }
  tax_years: "2025-2028"
capital_gains:
  single:
    - { min: 0, max: 49450, rate: 0.0 }
    - { min: 49450, max: 545500, rate: 0.15 }
    - { min: 545500, max: null, rate: 0.20 }
  mfj:
    - { min: 0, max: 98900, rate: 0.0 }
    - { min: 98900, max: 613700, rate: 0.15 }
    - { min: 613700, max: null, rate: 0.20 }
  mfs:
    - { min: 0, max: 49450, rate: 0.0 }
    - { min: 49450, max: 306850, rate: 0.15 }
    - { min: 306850, max: null, rate: 0.20 }
  hoh:
    - { min: 0, max: 66200, rate: 0.0 }
    - { min: 66200, max: 579600, rate: 0.15 }
    - { min: 579600, max: null, rate: 0.20 }
special_capital_gains:
  collectibles: 0.28
  unrecaptured_1250: 0.25
  qsbs_1202: 0.28
---

# Federal Income Tax (2026)

Source: Rev. Proc. 2025-32

Personal exemption remains 0 under TCJA/OBBBA.

Senior deduction (OBBBA §102) is separate from existing 65+/blind additional deduction.
