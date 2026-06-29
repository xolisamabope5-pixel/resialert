import requests

API_URL = "https://resialert.onrender.com/api/issue"

def send_issue(room, issue_type):
    payload = {
        "room": room,
        "type": issue_type
    }

    try:
        response = requests.post(API_URL, json=payload)

        try:
            print("\nResponse:", response.json())
        except Exception:
            print("\nResponse (not JSON):", response.text)

    except Exception as e:
        print("Request failed:", e)


# ----------------------------
# SIMPLE TEST MENU
# ----------------------------

while True:
    print("\nRESIALERT")
    print("1. Electricity")
    print("2. Water")
    print("3. Internet")
    print("4. Other")
    print("5. Exit")

    choice = input("Press button: ")

    if choice == "5":
        break

    room = input("Enter room number: ")

    mapping = {
        "1": "Electricity",
        "2": "Water",
        "3": "Internet",
        "4": "Other"
    }

    issue = mapping.get(choice, "Other")
    send_issue(room, issue)