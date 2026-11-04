"""Unit tests for the educational Windows Event CSV triage helper."""
import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "windows_event_csv_triage.py"
SPEC = importlib.util.spec_from_file_location("windows_event_csv_triage", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class EventIdFieldTests(unittest.TestCase):
    def test_recognizes_common_event_id_headers(self):
        for header in ("EventID", "Event Id", "Event ID", "EventCode", "event_id"):
            with self.subTest(header=header):
                self.assertEqual(MODULE.find_event_id_field([header]), header)

    def test_returns_none_for_missing_header(self):
        self.assertIsNone(MODULE.find_event_id_field(["TimeCreated", "Provider"]))


class CsvInputTests(unittest.TestCase):
    def test_counts_event_ids_from_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["EventID", "Computer"])
                writer.writeheader()
                writer.writerows([
                    {"EventID": "4625", "Computer": "LAB-WIN"},
                    {"EventID": "4625", "Computer": "LAB-WIN"},
                    {"EventID": "4624", "Computer": "LAB-WIN"},
                ])

            counts = {}
            with path.open(encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                field = MODULE.find_event_id_field(reader.fieldnames)
                for row in reader:
                    value = (row.get(field) or "").strip()
                    if value:
                        counts[value] = counts.get(value, 0) + 1

            self.assertEqual(counts, {"4625": 2, "4624": 1})


if __name__ == "__main__":
    unittest.main()
