import csv
from datetime import date, timedelta

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

def get_latest_rate(filename):
    rows = read_series_csv(filename)
    parsed_rows = parse_rows(rows)
    return parsed_rows[-1]

if __name__ == "__main__":
    recent_date, recent_rate = get_latest_rate("./mortgage30us.csv")
    today_date = date.today()
    diff = today_date - recent_date
    if diff.days == 0:
        print(f"The mortgage rate data updated today, on {recent_date.strftime("%a, %b %d")}. It is at {recent_rate}%.")
    elif diff.days == 1:
        print(f"The mortgage rate data updated yesterday on {recent_date.strftime("%B %dth, %Y")}. It was at {recent_rate}%.")
    else:
        print(f"The morgage rate date published {diff.days} days ago. It was at {recent_rate}%.")
    #sample = sample_parsed(parsed_rows, date(2026, 4, 1))
    #print(f"Last two months: {len(sample)} rows")
