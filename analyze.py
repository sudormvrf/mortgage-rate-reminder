import csv
from datetime import date

def read_series_csv(filename):
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def print_some_data(rows):
    print(f"Loaded {len(rows)} rows")
    print(f"First row is: \n{rows[0]}")
    print(f"Last row is: \n{rows[-1]}")
    print()
    missing = [r for r in rows if r["value"] == "."]
    print(f"Missing: {len(missing)}")
    print()
    valid_floats = [float(r["value"]) for r in rows if r["value"] != "."]
    print(f"Min: {min(valid_floats)}% Max: {max(valid_floats)}%")

def parse_rows(rows):
    return [
        (date.fromisoformat(r["date"]), float(r["value"]))
        for r in rows
    ]

def sample_parsed(parsed, since):
     return [(d, v) for (d, v) in parsed if d >= since]


if __name__ == "__main__":
    rows = read_series_csv("./mortgage30us.csv")
    print_some_data(rows)
    parsed_rows = parse_rows(rows)
    sample = sample_parsed(parsed_rows, date(2026, 4, 1))
    print(f"Last two months: {len(sample)} rows")
    pass
