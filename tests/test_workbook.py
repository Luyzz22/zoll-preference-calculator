import pathlib
import subprocess
import sys
import tempfile
import unittest
import pandas as pd
from openpyxl import load_workbook

ROOT = pathlib.Path(__file__).resolve().parents[1]

class WorkbookTest(unittest.TestCase):
    def run_script(self, work):
        return subprocess.run([sys.executable, str(ROOT / "preferences.py")], cwd=work, capture_output=True, text=True)

    def test_synthetic_example(self):
        with tempfile.TemporaryDirectory() as directory:
            work = pathlib.Path(directory)
            subprocess.run([sys.executable, str(ROOT / "create_input.py")], cwd=work, check=True, capture_output=True)
            result = self.run_script(work)
            self.assertEqual(result.returncode, 0, result.stderr)
            frame = pd.read_excel(work / "Output.xlsx")
            self.assertEqual(frame["EU_Anteil_Prozent"].tolist(), [70, 40, 62.5, 75, 20])
            self.assertEqual(frame["Präferenzursprung"].tolist(), ["JA", "NEIN", "JA", "JA", "NEIN"])
            book = load_workbook(work / "Output.xlsx")
            self.assertEqual(book.active["A2"].fill.fgColor.rgb[-6:], "90EE90")
            self.assertEqual(book.active["A3"].fill.fgColor.rgb[-6:], "FFB6C1")
            book.close()

    def test_invalid_costs_do_not_produce_a_result(self):
        for total, part in [(0, 1), (-1, 0), (100, -1), (100, 101), ("bad", 1), (100, float("inf"))]:
            with self.subTest(total=total, part=part), tempfile.TemporaryDirectory() as directory:
                work = pathlib.Path(directory)
                pd.DataFrame([{"Warennummer": "DEMO", "Lieferland": "DEMO", "Materialkosten_Gesamt": total, "EU_Anteil": part}]).to_excel(work / "Input.xlsx", index=False)
                self.assertNotEqual(self.run_script(work).returncode, 0)
                self.assertFalse((work / "Output.xlsx").exists())

    def test_missing_input_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertNotEqual(self.run_script(pathlib.Path(directory)).returncode, 0)

if __name__ == "__main__":
    unittest.main()
