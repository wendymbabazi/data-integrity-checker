# Simple script to check for missing data in a list of user records
users = [
    {"id": 1, "name": "Wendy", "email": "wendy@example.com"},
    {"id": 2, "name": "John", "email": ""},  # Error: Missing email
    {"id": 3, "name": "", "email": "admin@tech.com"}, # Error: Missing name
]

def check_integrity(data):
    print("--- Starting Data Integrity Audit ---")
    for record in data:
        if not record["name"] or not record["email"]:
            print(f"ALERT: Integrity Issue found in Record ID {record['id']}")
        else:
            print(f"Record ID {record['id']} is valid.")

check_integrity(users)
