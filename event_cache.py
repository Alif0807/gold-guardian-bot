import json
from pathlib import Path

CACHE_FILE = Path("event_cache.json")

def load_cache():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return []

def save_cache(events):
    with open(CACHE_FILE, "w") as f:
        json.dump(events, f)
