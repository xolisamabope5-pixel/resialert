import requests

DEVICES = {
    "1": {"room": "101", "name": "Room 101 Device"},
    "2": {"room": "223", "name": "Room 223 Device"},
    "3": {"room": "305", "name": "Room 305 Device"},
}

def send_issue(room, issue):
    data = {
        "room": room,
        "issue": issue,
        "device_id": f"esp32_room_{room}"
    }

    response = requests.post(
        "http://127.0.0.1:5000/report",
        json=data,
        timeout=5
    )

    print("\nResponse:", response.json())


print("SELECT DEVICE")
for key, device in DEVICES.items():
    print(f"{key}. {device['name']}")

device_choice = input("\nChoose device: ")

if device_choice not in DEVICES:
    print("Invalid device")
    exit()

room = DEVICES[device_choice]["room"]

while True:
    print(f"\nRESIALERT - {room}")
    print("1. Electricity")
    print("2. Water")
    print("3. Internet")
    print("4. Other")
    print("5. Exit")

    choice = input("Press button: ")

    if choice == "1":
        send_issue(room, "Electricity")

    elif choice == "2":
        send_issue(room, "Water")

    elif choice == "3":
        send_issue(room, "Internet")

    elif choice == "4":
        send_issue(room, "Other")

    elif choice == "5":
        break

    else:
        print("Invalid button")