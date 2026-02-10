---
states:
  AL:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 500, rate: 0.02 }
        - { min: 500, max: 3000, rate: 0.04 }
        - { min: 3000, max: null, rate: 0.05 }
      mfj:
        - { min: 0, max: 1000, rate: 0.02 }
        - { min: 1000, max: 6000, rate: 0.04 }
        - { min: 6000, max: null, rate: 0.05 }
      mfs:
        - { min: 0, max: 500, rate: 0.02 }
        - { min: 500, max: 3000, rate: 0.04 }
        - { min: 3000, max: null, rate: 0.05 }
      hoh:
        - { min: 0, max: 500, rate: 0.02 }
        - { min: 500, max: 3000, rate: 0.04 }
        - { min: 3000, max: null, rate: 0.05 }
  AR:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 5500, rate: 0.0 }
        - { min: 5500, max: 10900, rate: 0.02 }
        - { min: 10900, max: 15600, rate: 0.03 }
        - { min: 15600, max: 25700, rate: 0.034 }
        - { min: 25700, max: null, rate: 0.039 }
      mfj:
        - { min: 0, max: 5500, rate: 0.0 }
        - { min: 5500, max: 10900, rate: 0.02 }
        - { min: 10900, max: 15600, rate: 0.03 }
        - { min: 15600, max: 25700, rate: 0.034 }
        - { min: 25700, max: null, rate: 0.039 }
      mfs:
        - { min: 0, max: 5500, rate: 0.0 }
        - { min: 5500, max: 10900, rate: 0.02 }
        - { min: 10900, max: 15600, rate: 0.03 }
        - { min: 15600, max: 25700, rate: 0.034 }
        - { min: 25700, max: null, rate: 0.039 }
      hoh:
        - { min: 0, max: 5500, rate: 0.0 }
        - { min: 5500, max: 10900, rate: 0.02 }
        - { min: 10900, max: 15600, rate: 0.03 }
        - { min: 15600, max: 25700, rate: 0.034 }
        - { min: 25700, max: null, rate: 0.039 }
  CA:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 11079, rate: 0.01 }
        - { min: 11079, max: 26264, rate: 0.02 }
        - { min: 26264, max: 41452, rate: 0.04 }
        - { min: 41452, max: 57542, rate: 0.06 }
        - { min: 57542, max: 72724, rate: 0.08 }
        - { min: 72724, max: 371479, rate: 0.093 }
        - { min: 371479, max: 445771, rate: 0.103 }
        - { min: 445771, max: 742953, rate: 0.113 }
        - { min: 742953, max: 1000000, rate: 0.123 }
        - { min: 1000000, max: null, rate: 0.133 }
      mfj:
        - { min: 0, max: 22158, rate: 0.01 }
        - { min: 22158, max: 52528, rate: 0.02 }
        - { min: 52528, max: 82904, rate: 0.04 }
        - { min: 82904, max: 115084, rate: 0.06 }
        - { min: 115084, max: 145448, rate: 0.08 }
        - { min: 145448, max: 742958, rate: 0.093 }
        - { min: 742958, max: 891542, rate: 0.103 }
        - { min: 891542, max: 1000000, rate: 0.113 }
        - { min: 1000000, max: 1485906, rate: 0.123 }
        - { min: 1485906, max: null, rate: 0.133 }
      mfs:
        - { min: 0, max: 11079, rate: 0.01 }
        - { min: 11079, max: 26264, rate: 0.02 }
        - { min: 26264, max: 41452, rate: 0.04 }
        - { min: 41452, max: 57542, rate: 0.06 }
        - { min: 57542, max: 72724, rate: 0.08 }
        - { min: 72724, max: 371479, rate: 0.093 }
        - { min: 371479, max: 445771, rate: 0.103 }
        - { min: 445771, max: 742953, rate: 0.113 }
        - { min: 742953, max: 1000000, rate: 0.123 }
        - { min: 1000000, max: null, rate: 0.133 }
      hoh:
        - { min: 0, max: 22171, rate: 0.01 }
        - { min: 22171, max: 52530, rate: 0.02 }
        - { min: 52530, max: 67717, rate: 0.04 }
        - { min: 67717, max: 83809, rate: 0.06 }
        - { min: 83809, max: 98991, rate: 0.08 }
        - { min: 98991, max: 507743, rate: 0.093 }
        - { min: 507743, max: 609288, rate: 0.103 }
        - { min: 609288, max: 1000000, rate: 0.113 }
        - { min: 1000000, max: 1016470, rate: 0.123 }
        - { min: 1016470, max: null, rate: 0.133 }
  CT:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 10000, rate: 0.02 }
        - { min: 10000, max: 50000, rate: 0.045 }
        - { min: 50000, max: 100000, rate: 0.055 }
        - { min: 100000, max: 200000, rate: 0.06 }
        - { min: 200000, max: 250000, rate: 0.065 }
        - { min: 250000, max: 500000, rate: 0.069 }
        - { min: 500000, max: null, rate: 0.0699 }
      mfj:
        - { min: 0, max: 20000, rate: 0.02 }
        - { min: 20000, max: 100000, rate: 0.045 }
        - { min: 100000, max: 200000, rate: 0.055 }
        - { min: 200000, max: 400000, rate: 0.06 }
        - { min: 400000, max: 500000, rate: 0.065 }
        - { min: 500000, max: 1000000, rate: 0.069 }
        - { min: 1000000, max: null, rate: 0.0699 }
      mfs:
        - { min: 0, max: 10000, rate: 0.02 }
        - { min: 10000, max: 50000, rate: 0.045 }
        - { min: 50000, max: 100000, rate: 0.055 }
        - { min: 100000, max: 200000, rate: 0.06 }
        - { min: 200000, max: 250000, rate: 0.065 }
        - { min: 250000, max: 500000, rate: 0.069 }
        - { min: 500000, max: null, rate: 0.0699 }
      hoh:
        - { min: 0, max: 16000, rate: 0.02 }
        - { min: 16000, max: 80000, rate: 0.045 }
        - { min: 80000, max: 160000, rate: 0.055 }
        - { min: 160000, max: 320000, rate: 0.06 }
        - { min: 320000, max: 400000, rate: 0.065 }
        - { min: 400000, max: 800000, rate: 0.069 }
        - { min: 800000, max: null, rate: 0.0699 }
  DC:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 10000, rate: 0.04 }
        - { min: 10000, max: 40000, rate: 0.06 }
        - { min: 40000, max: 60000, rate: 0.065 }
        - { min: 60000, max: 250000, rate: 0.085 }
        - { min: 250000, max: 500000, rate: 0.0925 }
        - { min: 500000, max: 1000000, rate: 0.0975 }
        - { min: 1000000, max: null, rate: 0.1075 }
      mfj:
        - { min: 0, max: 10000, rate: 0.04 }
        - { min: 10000, max: 40000, rate: 0.06 }
        - { min: 40000, max: 60000, rate: 0.065 }
        - { min: 60000, max: 250000, rate: 0.085 }
        - { min: 250000, max: 500000, rate: 0.0925 }
        - { min: 500000, max: 1000000, rate: 0.0975 }
        - { min: 1000000, max: null, rate: 0.1075 }
      mfs:
        - { min: 0, max: 10000, rate: 0.04 }
        - { min: 10000, max: 40000, rate: 0.06 }
        - { min: 40000, max: 60000, rate: 0.065 }
        - { min: 60000, max: 250000, rate: 0.085 }
        - { min: 250000, max: 500000, rate: 0.0925 }
        - { min: 500000, max: 1000000, rate: 0.0975 }
        - { min: 1000000, max: null, rate: 0.1075 }
      hoh:
        - { min: 0, max: 10000, rate: 0.04 }
        - { min: 10000, max: 40000, rate: 0.06 }
        - { min: 40000, max: 60000, rate: 0.065 }
        - { min: 60000, max: 250000, rate: 0.085 }
        - { min: 250000, max: 500000, rate: 0.0925 }
        - { min: 500000, max: 1000000, rate: 0.0975 }
        - { min: 1000000, max: null, rate: 0.1075 }
  DE:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 2000, rate: 0.0 }
        - { min: 2000, max: 5000, rate: 0.022 }
        - { min: 5000, max: 10000, rate: 0.039 }
        - { min: 10000, max: 20000, rate: 0.048 }
        - { min: 20000, max: 25000, rate: 0.052 }
        - { min: 25000, max: 60000, rate: 0.0555 }
        - { min: 60000, max: 125000, rate: 0.066 }
        - { min: 125000, max: 250000, rate: 0.0675 }
        - { min: 250000, max: null, rate: 0.0695 }
      mfj:
        - { min: 0, max: 2000, rate: 0.0 }
        - { min: 2000, max: 5000, rate: 0.022 }
        - { min: 5000, max: 10000, rate: 0.039 }
        - { min: 10000, max: 20000, rate: 0.048 }
        - { min: 20000, max: 25000, rate: 0.052 }
        - { min: 25000, max: 60000, rate: 0.0555 }
        - { min: 60000, max: 125000, rate: 0.066 }
        - { min: 125000, max: 250000, rate: 0.0675 }
        - { min: 250000, max: null, rate: 0.0695 }
      mfs:
        - { min: 0, max: 2000, rate: 0.0 }
        - { min: 2000, max: 5000, rate: 0.022 }
        - { min: 5000, max: 10000, rate: 0.039 }
        - { min: 10000, max: 20000, rate: 0.048 }
        - { min: 20000, max: 25000, rate: 0.052 }
        - { min: 25000, max: 60000, rate: 0.0555 }
        - { min: 60000, max: 125000, rate: 0.066 }
        - { min: 125000, max: 250000, rate: 0.0675 }
        - { min: 250000, max: null, rate: 0.0695 }
      hoh:
        - { min: 0, max: 2000, rate: 0.0 }
        - { min: 2000, max: 5000, rate: 0.022 }
        - { min: 5000, max: 10000, rate: 0.039 }
        - { min: 10000, max: 20000, rate: 0.048 }
        - { min: 20000, max: 25000, rate: 0.052 }
        - { min: 25000, max: 60000, rate: 0.0555 }
        - { min: 60000, max: 125000, rate: 0.066 }
        - { min: 125000, max: 250000, rate: 0.0675 }
        - { min: 250000, max: null, rate: 0.0695 }
  HI:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 9600, rate: 0.014 }
        - { min: 9600, max: 14400, rate: 0.032 }
        - { min: 14400, max: 19200, rate: 0.055 }
        - { min: 19200, max: 24000, rate: 0.064 }
        - { min: 24000, max: 36000, rate: 0.068 }
        - { min: 36000, max: 48000, rate: 0.072 }
        - { min: 48000, max: 125000, rate: 0.076 }
        - { min: 125000, max: 175000, rate: 0.079 }
        - { min: 175000, max: 225000, rate: 0.0825 }
        - { min: 225000, max: 275000, rate: 0.09 }
        - { min: 275000, max: 325000, rate: 0.10 }
        - { min: 325000, max: null, rate: 0.11 }
      mfj:
        - { min: 0, max: 19200, rate: 0.014 }
        - { min: 19200, max: 28800, rate: 0.032 }
        - { min: 28800, max: 38400, rate: 0.055 }
        - { min: 38400, max: 48000, rate: 0.064 }
        - { min: 48000, max: 72000, rate: 0.068 }
        - { min: 72000, max: 96000, rate: 0.072 }
        - { min: 96000, max: 250000, rate: 0.076 }
        - { min: 250000, max: 350000, rate: 0.079 }
        - { min: 350000, max: 450000, rate: 0.0825 }
        - { min: 450000, max: 550000, rate: 0.09 }
        - { min: 550000, max: 650000, rate: 0.10 }
        - { min: 650000, max: null, rate: 0.11 }
      mfs:
        - { min: 0, max: 9600, rate: 0.014 }
        - { min: 9600, max: 14400, rate: 0.032 }
        - { min: 14400, max: 19200, rate: 0.055 }
        - { min: 19200, max: 24000, rate: 0.064 }
        - { min: 24000, max: 36000, rate: 0.068 }
        - { min: 36000, max: 48000, rate: 0.072 }
        - { min: 48000, max: 125000, rate: 0.076 }
        - { min: 125000, max: 175000, rate: 0.079 }
        - { min: 175000, max: 225000, rate: 0.0825 }
        - { min: 225000, max: 275000, rate: 0.09 }
        - { min: 275000, max: 325000, rate: 0.10 }
        - { min: 325000, max: null, rate: 0.11 }
      hoh:
        - { min: 0, max: 19200, rate: 0.014 }
        - { min: 19200, max: 28800, rate: 0.032 }
        - { min: 28800, max: 38400, rate: 0.055 }
        - { min: 38400, max: 48000, rate: 0.064 }
        - { min: 48000, max: 72000, rate: 0.068 }
        - { min: 72000, max: 96000, rate: 0.072 }
        - { min: 96000, max: 250000, rate: 0.076 }
        - { min: 250000, max: 350000, rate: 0.079 }
        - { min: 350000, max: 450000, rate: 0.0825 }
        - { min: 450000, max: 550000, rate: 0.09 }
        - { min: 550000, max: 650000, rate: 0.10 }
        - { min: 650000, max: null, rate: 0.11 }
  KS:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 15000, rate: 0.031 }
        - { min: 15000, max: 30000, rate: 0.0525 }
        - { min: 30000, max: null, rate: 0.0558 }
      mfj:
        - { min: 0, max: 30000, rate: 0.031 }
        - { min: 30000, max: 60000, rate: 0.0525 }
        - { min: 60000, max: null, rate: 0.0558 }
      mfs:
        - { min: 0, max: 15000, rate: 0.031 }
        - { min: 15000, max: 30000, rate: 0.0525 }
        - { min: 30000, max: null, rate: 0.0558 }
      hoh:
        - { min: 0, max: 15000, rate: 0.031 }
        - { min: 15000, max: 30000, rate: 0.0525 }
        - { min: 30000, max: null, rate: 0.0558 }
  ME:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 26800, rate: 0.058 }
        - { min: 26800, max: 63450, rate: 0.0675 }
        - { min: 63450, max: null, rate: 0.0715 }
      mfj:
        - { min: 0, max: 53600, rate: 0.058 }
        - { min: 53600, max: 126900, rate: 0.0675 }
        - { min: 126900, max: null, rate: 0.0715 }
      mfs:
        - { min: 0, max: 26800, rate: 0.058 }
        - { min: 26800, max: 63450, rate: 0.0675 }
        - { min: 63450, max: null, rate: 0.0715 }
      hoh:
        - { min: 0, max: 40200, rate: 0.058 }
        - { min: 40200, max: 95150, rate: 0.0675 }
        - { min: 95150, max: null, rate: 0.0715 }
  MD:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 1000, rate: 0.02 }
        - { min: 1000, max: 2000, rate: 0.03 }
        - { min: 2000, max: 3000, rate: 0.04 }
        - { min: 3000, max: 100000, rate: 0.0475 }
        - { min: 100000, max: 125000, rate: 0.05 }
        - { min: 125000, max: 150000, rate: 0.0525 }
        - { min: 150000, max: 250000, rate: 0.055 }
        - { min: 250000, max: 500000, rate: 0.0575 }
        - { min: 500000, max: 1000000, rate: 0.0625 }
        - { min: 1000000, max: null, rate: 0.065 }
      mfj:
        - { min: 0, max: 1000, rate: 0.02 }
        - { min: 1000, max: 2000, rate: 0.03 }
        - { min: 2000, max: 3000, rate: 0.04 }
        - { min: 3000, max: 150000, rate: 0.0475 }
        - { min: 150000, max: 175000, rate: 0.05 }
        - { min: 175000, max: 225000, rate: 0.0525 }
        - { min: 225000, max: 300000, rate: 0.055 }
        - { min: 300000, max: 600000, rate: 0.0575 }
        - { min: 600000, max: 1200000, rate: 0.0625 }
        - { min: 1200000, max: null, rate: 0.065 }
      mfs:
        - { min: 0, max: 1000, rate: 0.02 }
        - { min: 1000, max: 2000, rate: 0.03 }
        - { min: 2000, max: 3000, rate: 0.04 }
        - { min: 3000, max: 75000, rate: 0.0475 }
        - { min: 75000, max: 87500, rate: 0.05 }
        - { min: 87500, max: 112500, rate: 0.0525 }
        - { min: 112500, max: 150000, rate: 0.055 }
        - { min: 150000, max: 300000, rate: 0.0575 }
        - { min: 300000, max: 600000, rate: 0.0625 }
        - { min: 600000, max: null, rate: 0.065 }
      hoh:
        - { min: 0, max: 1000, rate: 0.02 }
        - { min: 1000, max: 2000, rate: 0.03 }
        - { min: 2000, max: 3000, rate: 0.04 }
        - { min: 3000, max: 150000, rate: 0.0475 }
        - { min: 150000, max: 175000, rate: 0.05 }
        - { min: 175000, max: 225000, rate: 0.0525 }
        - { min: 225000, max: 300000, rate: 0.055 }
        - { min: 300000, max: 600000, rate: 0.0575 }
        - { min: 600000, max: 1200000, rate: 0.0625 }
        - { min: 1200000, max: null, rate: 0.065 }
  MA:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 1107750, rate: 0.05 }
        - { min: 1107750, max: null, rate: 0.09 }
      mfj:
        - { min: 0, max: 1107750, rate: 0.05 }
        - { min: 1107750, max: null, rate: 0.09 }
      mfs:
        - { min: 0, max: 1107750, rate: 0.05 }
        - { min: 1107750, max: null, rate: 0.09 }
      hoh:
        - { min: 0, max: 1107750, rate: 0.05 }
        - { min: 1107750, max: null, rate: 0.09 }
  MN:
    type: graduated
    brackets:
      single:
        - { min: 0, max: 33310, rate: 0.0535 }
        - { min: 33310, max: 109430, rate: 0.068 }
        - { min: 109430, max: 203150, rate: 0.0785 }
        - { min: 203150, max: null, rate: 0.0985 }
      mfj:
        - { min: 0, max: 48700, rate: 0.0535 }
        - { min: 48700, max: 193480, rate: 0.068 }
        - { min: 193480, max: 337930, rate: 0.0785 }
        - { min: 337930, max: null, rate: 0.0985 }
      mfs:
        - { min: 0, max: 24350, rate: 0.0535 }
        - { min: 24350, max: 96740, rate: 0.068 }
        - { min: 96740, max: 168965, rate: 0.0785 }
        - { min: 168965, max: null, rate: 0.0985 }
      hoh:
        - { min: 0, max: 41010, rate: 0.0535 }
        - { min: 41010, max: 164800, rate: 0.068 }
        - { min: 164800, max: 270060, rate: 0.0785 }
        - { min: 270060, max: null, rate: 0.0985 }
standard_deductions:
  AL: { single: 3000, mfj: 8500, mfs: 4250, hoh: 5200 }
  AR: { single: 2470, mfj: 4940, mfs: 2470, hoh: 2470 }
  CA: { single: 5706, mfj: 11412, mfs: 5706, hoh: 11412 }
  DE: { single: 3250, mfj: 6500, mfs: 3250, hoh: 3250 }
  KS: { single: 3500, mfj: 8000, mfs: 3500, hoh: 3500 }
  ME: { single: 15300, mfj: 30600, mfs: 15300, hoh: 22950 }
  MD: { single: 3350, mfj: 6700, mfs: 3350, hoh: 6700 }
  MN: { single: 15300, mfj: 30600, mfs: 15300, hoh: 23000 }
---

# Graduated Tax States: AL–MN (2026)

## Alabama
**Source:** [AL DOR](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) | **Data:** official_2026

Top rate 5%. MFJ brackets differ (1,000/6,000 vs 500/3,000). Sliding scale max deduction decreases with AGI above 20,499. Also allows federal tax deduction.

---

## Arkansas
**Source:** [AR DFA](https://www.dfa.arkansas.gov/income-tax-administration/withholding-tax-branch/withholding-tax-forms-instructions/) | **Data:** 2025_no_2026_update

Top rate 3.9%. Same brackets for all filing statuses. Capital gains: 50% exclusion. Top rate reduced from 4.4% in 2024.

---

## California
**Source:** [CA EDD](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf) | **Data:** official_2026

Top rate 13.3%. Capital gains: ordinary income. QBID: does NOT conform.

SDI: 1.3% on all wages (no cap since 2024). Mandatory for W-2 employees. Mental health surcharge: 1% on income over 1M (included in 13.3%).

2026 inflation-adjusted thresholds per CA FTB.

---

## Connecticut
**Source:** [CT DRS](https://portal.ct.gov/-/media/drs/forms/2025/wth/tpg-211_1225.pdf) | **Data:** official_2026

Top rate 6.99%. No standard deduction (uses personal exemption credits).

Personal exemption: Single 15,000 | MFJ 24,000 | MFS 12,000 | HOH 19,000 (credit, phases out).

---

## DC (District of Columbia)
**Source:** [DC OTR](https://otr.cfo.dc.gov/page/income-tax-withholding-instructions-and-tables) | **Data:** 2025_no_2026_update

Top rate 10.75%. Same brackets for all filing statuses. Standard deduction: uses federal amounts. QBID: does NOT conform.

S-Corp: not recognized (taxed as C-corp, Franchise Tax 8.25%, min 250).

---

## Delaware
**Source:** [DE DOR](https://revenue.delaware.gov/employers-guide-withholding-tables/) | **Data:** 2025_unchanged

Top rate 6.95%. Same brackets for all filing statuses. New high-income brackets per HB 13: 6.75% (125K-250K), 6.95% (>250K).

---

## Hawaii
**Source:** [HI DOTAX](https://tax.hawaii.gov/) | **Data:** 2025_no_2026_update

Top rate 11%. HOH uses same brackets as MFJ. QBID: does NOT conform.

PTET: available (Act 50, 2023) - uses individual rates (1.4%-11%).

---

## Kansas
**Source:** [KS DOR](https://www.ksrevenue.gov/) | **Data:** official_2026

Top rate 5.58%. MFS and HOH use same brackets as single.

PTET: 5.58% rate, refundable credit.

---

## Maine
**Source:** [ME Revenue](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr.pdf) | **Data:** official_2026

Top rate 7.15%. Personal exemption: 5,300.

Standard deduction phases out for Single >102,250 and MFJ >204,550. PTET: 7.15% rate, refundable credit.

---

## Maryland
**Source:** [MD Comptroller](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf) | **Data:** official_2026

Top rate 6.5%. Local tax: counties add 2.25%-3.30% (max increased from 3.2%). Capital gains surtax: 2% on income >350K.

New brackets: 6.25% (500K-1M), 6.5% (>1M). PTET: 5.75%+local rate, refundable credit.

---

## Massachusetts
**Source:** [MA DOR](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) | **Data:** official_2026

Top rate 9%. Same brackets for all filing statuses. No standard deduction (uses personal exemptions).

Personal exemption: Single 4,400 | MFJ 8,800 | MFS 4,400 | HOH 6,800 | Additional 65+/blind 700.

4% millionaire surtax on income over ~1.1M (threshold inflation-adjusted from 1M base). PTET: 5% rate, refundable credit.

---

## Minnesota
**Source:** [MN DOR](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) | **Data:** official_2026

Top rate 9.85%. Dependent exemption: 5,300. Capital gains: ordinary income. QBID: does NOT conform.

PTET: EXPIRED Dec 31, 2025 - NOT available for 2026 (former rate 9.85%). 2026 inflation-adjusted thresholds (2.369% from 2025).
