#!/usr/bin/env python3
"""Convert between Gregorian (CE), Anno Computatri (AC) and Unix time.

Anno Computatri counts years from 1970, the Unix epoch: AC year = CE year - 1970.
Months, days and times are Gregorian; all times are UTC.

Usage:
  python ac.py now                         current moment
  python ac.py ce 2026-10-05               CE date (time optional: "2026-10-05 14:30:00")
  python ac.py ac 56-10-05                 AC date (negative years allowed: "-1-07-20 20:17:40")
  python ac.py unix 1767225600             Unix timestamp in seconds (negative allowed)
  python ac.py year 1066                   year only (any CE year; use -499 for 500 BCE)
  add --json for machine-readable output
"""
import json
import re
import sys
from datetime import datetime, timedelta, timezone

EPOCH_YEAR = 1970
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
DATE_RE = re.compile(r"^\s*(-?\d+)-(\d{1,2})-(\d{1,2})(?:[ T](\d{1,2}):(\d{2})(?::(\d{2}))?)?\s*$")


def from_datetime(dt):
    dt = dt.astimezone(timezone.utc)
    ac_year = dt.year - EPOCH_YEAR
    rest = dt.strftime("%m-%d %H:%M:%S")
    return {
        "ce": f"{dt.year:04d}-{rest}",
        "ac": f"{ac_year}-{rest}",
        "ac_formatted": f"⏀ {ac_year}-{rest}",
        "ac_year": ac_year,
        "unix": int((dt - EPOCH).total_seconds()),
    }


def parse(text):
    m = DATE_RE.match(text)
    if not m:
        raise ValueError(f"cannot parse date {text!r}; use YEAR-MM-DD [HH:MM[:SS]]")
    y, mo, d, h, mi, s = (int(g) if g else 0 for g in m.groups())
    return y, mo, d, h, mi, s


def make(y, mo, d, h, mi, s):
    if not 1 <= y <= 9999:
        raise ValueError("full dates are supported for CE years 1-9999; use 'year' for others")
    return datetime(y, mo, d, h, mi, s, tzinfo=timezone.utc)


def year_only(ce_year):
    ac_year = ce_year - EPOCH_YEAR
    era = f"{ce_year} CE" if ce_year >= 1 else f"{1 - ce_year} BCE"
    return {"ce_year": ce_year, "ce_label": era, "ac_year": ac_year, "ac_label": f"{ac_year} AC"}


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    if not args:
        sys.exit(__doc__)
    mode, value = args[0], " ".join(args[1:])
    if mode == "now":
        result = from_datetime(datetime.now(timezone.utc))
    elif mode == "ce":
        result = from_datetime(make(*parse(value)))
    elif mode == "ac":
        y, *rest = parse(value.replace("⏀", ""))
        result = from_datetime(make(y + EPOCH_YEAR, *rest))
    elif mode == "unix":
        result = from_datetime(EPOCH + timedelta(seconds=int(value)))
    elif mode == "year":
        result = year_only(int(value))
    else:
        sys.exit(f"unknown mode {mode!r}\n{__doc__}")

    if as_json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        for key, val in result.items():
            print(f"{key}: {val}")


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except (ValueError, OverflowError) as err:
        sys.exit(f"error: {err}")
