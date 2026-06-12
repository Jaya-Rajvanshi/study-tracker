import json # branch-b was here
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_subject(data):
    name = input("Enter subject name: ").strip()
    if name in data:
        print(f"'{name}' already exists")
    else:
        data[name] = {"total_hours": 0, "sessions": []}
        save_data(data)
        print(f"Subject '{name}' added successfully")
        
def view_progress(data):
    if not data:
        print("No subjects found. Add a subject first")
        return
    print("\n--- Study Progress ---")
    for subject, info in data.items():
        sessions = len(info["sessions"])
        total = info["total_hours"]
        print(f"{subject}: {total} total hours across {sessions} session(s)")
    print("----------------------")
    
