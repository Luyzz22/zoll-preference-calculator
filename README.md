# Percentage calculation with Excel output

An educational Python prototype that reads material-cost values from Excel, calculates their percentage share and colors the result. The fixed **50% threshold is a demonstration assumption**. The implementation contains no agreement-specific or tariff-specific origin rules and must not be used to determine customs eligibility.

## Run the example

```bash
git clone https://github.com/Luyzz22/zoll-preference-calculator.git
cd zoll-preference-calculator
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python create_input.py
python preferences.py
```

On Windows, activate with `.venv\Scripts\activate`. `create_input.py` writes five synthetic rows to `Input.xlsx`, overwriting an existing file of that name. Run examples in a separate working directory.

## Input and output

| Column | Use |
| --- | --- |
| `Warennummer` | Carried through; no tariff rule lookup is performed. |
| `Lieferland` | Carried through; no agreement lookup is performed. |
| `Materialkosten_Gesamt` | Positive finite total cost. |
| `EU_Anteil` | Finite component cost between zero and total cost. |

The script writes `Output.xlsx` with `EU_Anteil_Prozent` and historical result columns `Präferenzursprung` / `Status`. `JA` means only that the demo threshold was reached. These column names are retained for compatibility, not as a legal finding.

## Verify

```bash
python -m unittest discover -s tests -v
```

The tests run the actual command in temporary directories. They check the example workbook, percentages and missing/invalid input handling. GitHub Actions repeats them with Python 3.12.

## Boundaries

No SAP connection, API, maintained legal rules or production workflow is implemented. Earlier production-readiness and blanket compliance claims have been removed. Input files and generated reports are excluded from new commits; historical copies remain in Git history.

Maintained by [Luis Schenk](https://github.com/Luyzz22). Current commercial work is described at [SBS Deutschland](https://sbsdeutschland.com/).
