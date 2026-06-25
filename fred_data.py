import requests
import time
import csv
import config

API_KEY = config.fred_api_key
BASE_URL = "https://api.stlouisfed.org/fred"

def get_category(category_id):
    params = {
        "category_id": category_id,
        "api_key": API_KEY,
        "file_type": "json",
    }

    r = requests.get(f"{BASE_URL}/category", params=params, timeout=10)
    r.raise_for_status()
    obs = r.json()["categories"]
    return obs

def get_category_children(parent_id):
    params = {
        "category_id": parent_id,
        "api_key": API_KEY,
        "file_type": "json",
    }
    
    r = requests.get(f"{BASE_URL}/category/children", params=params, timeout=10)
    r.raise_for_status()
    return r.json()["categories"]

def get_category_series(category_id):
    params = {
        "category_id": category_id,
        "api_key": API_KEY,
        "file_type": "json",
    }

    r = requests.get(f"{BASE_URL}/category/series", params=params, timeout=10)
    r.raise_for_status()
    return r.json()["seriess"]

def get_series_observations(series_id, start=None, end=None):
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json",
    }
    if start:
        params["observation_start"] = start  # YYYY-MM-DD
    if end:
        params["observation_end"] = end

    r = requests.get(f"{BASE_URL}/series/observations", params=params, timeout=10)
    r.raise_for_status()
    return r.json()["observations"]

def print_all_categories():
    for child in get_category_children(0):
        try:
            print("This is the parent:")
            print(f'{child['id']}, "{child['name']}"')
            print()
            print("These are the children:")
            for sub in get_category_children(child['id']):
                print(f'{sub['id']}, "{sub['name']}"')
            print()    
            time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            print(f"{child}: failed ({e})")

def write_all_categories_csv(filename):        
    with open(filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "parent_id"])

        for top in get_category_children(0):
            w.writerow([top['id'], top['name'], 0])
            for sub in get_category_children(top['id']):
                w.writerow([sub['id'], sub['name'], sub['parent_id']])

def write_series_csv(series_id, filename, start=None):
    obs = get_series_observations(series_id, start=start)
    with open(filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "value"])
        for o in obs:
            w.writerow([o["date"], o["value"]])

def print_series_in_category(category_id):
    for s in get_category_series(category_id):
        print(f"{s['id']:20} {s['frequency_short']:3} {s['title']}")

def print_series_observations(series_id, start):
    for obs in get_series_observations(series_id, start):
        print(f"{obs['date']} {obs['value']}")
        
if __name__ == "__main__":
    write_series_csv("MORTGAGE30US", "mortgage30us.csv")
    pass
