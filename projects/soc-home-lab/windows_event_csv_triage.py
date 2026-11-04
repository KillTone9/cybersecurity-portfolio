#!/usr/bin/env python3
"""Summarize Windows event IDs from an exported CSV file.

This is a small educational helper for sanitized lab exports. It does not
determine whether an event is malicious and does not replace SIEM analysis.
Uses only the Python standard library.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


EVENT_ID_FIELDS = ("EventID", "Event Id", "Event ID", "EventCode", "event_id")


def find_event_id_field(fieldnames: list[str] | None) -> str | None:
    if not fieldnames:
        return None
    normalized = {name.strip().lower(): name for name in fieldnames}
    for candidate in EVENT_ID_FIELDS:
        match = normalized.get(candidate.lower())
        if match:
            return match
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Count event IDs in a Windows Event Viewer CSV export."
    )
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    if not args.csv_file.is_file():
        parser.error(f"File not found: {args.csv_file}")

    counts: Counter[str] = Counter()
    total = 0
    skipped = 0

    with args.csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        event_field = find_event_id_field(reader.fieldnames)
        if not event_field:
            parser.error(
                "Could not identify an Event ID column. Expected EventID, "
                "Event Id, Event ID, or EventCode."
            )

        for row in reader:
            total += 1
            value = (row.get(event_field) or "").strip()
            if value:
                counts[value] += 1
            else:
                skipped += 1

    print(f"Rows processed: {total}")
    print(f"Rows without an event ID: {skipped}")
    print("\nEvent ID counts:")
    for event_id, count in counts.most_common():
        print(f"  {event_id:<12} {count}")

    print(
        "\nTriage reminder: frequency alone does not establish malicious activity. "
        "Correlate events with host, account, time, and surrounding activity."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
