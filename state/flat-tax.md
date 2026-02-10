---
states:
  AZ: { type: flat, rate: 0.025 }
  CO: { type: flat, rate: 0.044 }
  GA:
    type: flat
    rate: 0.0509
    dependent_exemption: 4000
  ID: { type: flat, rate: 0.053 }
  IL: { type: flat, rate: 0.0495 }
  IN: { type: flat, rate: 0.0295 }
  IA: { type: flat, rate: 0.038 }
  KY: { type: flat, rate: 0.035 }
  LA: { type: flat, rate: 0.03 }
  MI:
    type: flat
    rate: 0.0425
    personal_exemption: 5900
    senior_deduction: { single: 20000, mfj: 40000 }
  MO: { type: flat, rate: 0.047 }
  MS:
    type: graduated
    brackets:
      - { min: 0, max: 10000, rate: 0.0 }
      - { min: 10000, max: null, rate: 0.04 }
    personal_exemption: { single: 6000, mfj: 12000, hoh: 9500, dependent: 1500 }
  NC: { type: flat, rate: 0.0399 }
  OH:
    type: graduated
    brackets:
      - { min: 0, max: 26050, rate: 0.0 }
      - { min: 26050, max: null, rate: 0.0275 }
    personal_exemption: 650
    personal_exemption_magi_limit: 500000
    business_income_rate: 0.03
  PA: { type: flat, rate: 0.0307 }
  UT: { type: flat, rate: 0.045 }
standard_deductions:
  AZ: { single: 15750, mfj: 31500, mfs: 15750, hoh: 23625 }
  GA: { single: 12000, mfj: 24000, mfs: 12000, hoh: 12000 }
  KY: { single: 3160, mfj: 3160, mfs: 3160, hoh: 3160 }
  LA: { single: 12875, mfj: 25750, mfs: 12875, hoh: 25750 }
  MS: { single: 2300, mfj: 4600, mfs: 2300, hoh: 3400 }
  NC: { single: 12750, mfj: 25500, mfs: 12750, hoh: 19125 }
---

# Flat Tax States (2026)

## Arizona
[AZ DOR](https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4_f.pdf) | official_2026

Own standard deduction, indexed annually. May reduce to 2.42% if revenue triggers met per SB 1318.

## Colorado
[CO DOR](https://tax.colorado.gov/sites/tax/files/documents/DR_1098_Colorado_Withholding_Worksheet_for_Employees.pdf) | official_2026

Uses federal taxable income as starting point (no state standard deduction).

## Georgia
[GA DOR](https://dor.georgia.gov/document/document/2026-employers-tax-guide/download) | official_2026

5.09% effective Jan 1, 2026 per HB 111 annual 0.10% reduction (was 5.19% in 2025).

## Idaho
[ID Tax Commission](https://tax.idaho.gov/) | official_2026

5.3% reduced per HB 40 (was 5.75%).

## Illinois
[IL DOR](https://tax.illinois.gov/) | official_2026

1.5% replacement tax on S-corps. PTET permanent (sunset removed December 2025).

## Indiana
[IN DOR](https://www.in.gov/dor/) | official_2026

Counties add 0.5%-3.38% local tax.

## Iowa
[IA DOR](https://tax.iowa.gov/) | official_2026

## Kentucky
[KY DOR](https://revenue.ky.gov/Forms/2026%20Withholding%20Formula.pdf) | official_2026

3.5% effective Jan 1, 2026 per HB 1 (reduced from 4.0%).

## Louisiana
[LA DOR](https://dam.ldr.la.gov/taxforms/1306-1-26.pdf) | official_2026

Combined deduction+exemption effective 2025. Dependent exemptions eliminated. Adjusted annually for inflation starting 2026.

## Michigan
[MI Treasury](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) | official_2026

Personal exemption: 5,900 per person and per dependent. Senior deduction age 67+. Some cities have local tax (Detroit 2.4% resident, 1.2% non-resident).

## Mississippi
[MS DOR](https://www.dor.ms.gov/sites/default/files/Business/89700241.pdf) | official_2026

First 10,000 exempt. 4% flat on income over exemption (reduced from 4.4% in 2025). Same brackets all filing statuses.

## Missouri
[MO DOR](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) | official_2026

4.7% flat effective Jan 1, 2026 per HB 798 (SB 458 for 4% NOT enacted). Federal conformity standard deduction. Additional deductions for age 65+/blind.

## North Carolina
[NC DOR](https://www.ncdor.gov/taxes-forms/withholding-tax/withholding-tables-and-instructions-employers) | official_2026

3.99% effective Jan 1, 2026 (reduced from 4.25% in 2025).

## Ohio
[OH Tax](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2025-2026%20NYP%20Updates/2026_OH_Employer_School_District_Withholding_Tax_Filing_Guidelines.pdf) | official_2026

Personal exemption unavailable for MAGI >500K starting 2026. Business income taxed at 3.0% flat. 600+ cities have municipal income tax (0.5%-3%). Same brackets all filing statuses. PTET: CAT only (exclusion basis).

## Pennsylvania
[PA DOR](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/employerwithholding/documents/rev-580.pdf) | official_2026

PA uses 8 classes of income with limited deductions, no federal AGI concept. Tax Forgiveness program for low/moderate-income. Most municipalities have Earned Income Tax (1%-3.9%). QBID does NOT conform.

## Utah
[UT Tax](https://tax.utah.gov/forms/pubs/pub-14.pdf) | 2025_rolling_pub

4.5% effective 2026 per HB 106 (reduced from 4.55%). Uses tax credit system: 6% of federal deductions (excluding state tax deduction) + personal exemption (2,046), phases out at higher incomes. PTET availability tied to federal SALT cap existence.
