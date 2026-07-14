# 🚗 US Auto Import & Repair Calculator (Ukraine)

A comprehensive Python command-line utility designed to estimate the total "ready-to-drive" cost of importing and restoring a vehicle from US salvage auctions (such as Copart or IAAI) to Ukraine. 

This program automates the calculation of auction fees, ocean logistics, custom clearances (including duty, excise, and VAT based on Ukrainian tax codes), and local registration fees.

---

## 📊 Features

* **Copart Buyer Fees:** Simulates the actual progressive 2026 standard buyer fee tiers, including internet and gate processing fees.
* **Complex Customs Clearance:** Computes real-world Ukrainian customs taxes:
  * **Import Duty:** $10\%$ of the vehicle value plus auction fees.
  * **Excise Tax:** Calculates based on engine volume, fuel type (gasoline/diesel), and car age using Ukrainian tax rates.
  * **VAT (НДС):** $20\%$ of the combined customs value, import duty, and excise tax.
* **Logistics Engine:** Breakdown of multi-stage shipping including US land transport, sea freight, European port fees, and delivery to Ukrainian customs.
* **Local Taxes & Setup:** Calculates progressive Pension Fund registration fees ($3\%$, $4\%$, or $5\%$) alongside certification and license plate costs.
* **Investment Analyzer:** Compares the estimated grand total with current Ukrainian market values to assess financial viability.
* **Modern Terminal UI:** Built with the `rich` library, outputting beautifully organized, clean, and color-coded financial tables.

---

## 🛠️ Project Architecture

```text
USAutoImportCalc/
│
├── main.py        # Interactive CLI, input validation, and final table reports
├── calculator.py  # Core calculation logic (Excise, VAT, Logistics, and Pension Fund)
├── rates.py       # Hardcoded 2026 auction fee tiers, transport fees, and constants
└── .gitignore     # Prevents local cache files from being committed to git
