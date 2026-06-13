import json # branch-a was here
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

def log_hours(data):
    if not data:
        print("No subjects found. Add a subject first")
        return
    print("\nYour Subjects:")
    for subject in data:
        print(f" - {subject}")    
    name = input("Enter subject name to log hours: ").strip()
    if name not in data:
        print(f"Subject {name} not found.")
        return
    try:
        hours = float(input(f"How many hours did you study '{name}' today? "))
        data[name]["total_hours"]+= hours
        data[name]["sessions"].append(hours)
        save_data(data)
        print(f"Logged {hours} hours for '{name}'. Total: {data[name]['total_hours']} hours.")
    except ValueError:
        print("Please enter a valid number.")
        
def delete_subject(data):
    if not data:
        print("No subjects found.")
        return
    print("\nYour Subjects: ")
    for subject in data:
        print(f" - {subject}")
    name = input("Enter subject name to delete: ").strip()
    if name not in data:
        print(f"Subject '{name}' not found.")
        return
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del data[name]
        save_data(data)
        print(f"Subject '{name}' deleted.")
    else:
        print("Deletion cancelled")
        
def main():
    data = load_data()
    while True:
        print("\n===== Study Tracker =====")
        print("1. Add subject")
        print("2. Log study hours")
        print("3. View progress")
        print("4. Delete subject")
        print("5. Exit")
        print("=========================")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_subject(data)
        elif choice == "2":
            log_hours(data)
        elif choice == "3":
            view_progress(data)
        elif choice == "4":
            delete_subject(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
        
if __name__ == "__main__":
    main()
    
    
    
