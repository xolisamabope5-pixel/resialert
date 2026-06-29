import requests

# Each device is now permanently linked to ONE room
ROOM = "223"


def send_issue(issue):
    data = {
        "room": ROOM,
        "issue": issue,
        "device_id": f"esp32_room_{ROOM}"
    }

    try:
        response = requests.post(
            "http://127.0.0.1:5000/report",
            json=data,
            timeout=5
        )
        print("\nServer response:")
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Error sending request:", e)


while True:
    print("\nRESIALERT DEVICE (ROOM:", ROOM, ")")
    print("1. Electricity")
    print("2. Water")
    print("3. Internet")
    print("4. Other")
    print("5. Exit")

    choice = input("Press button: ")

    if choice == "1":
        send_issue("Electricity")

    elif choice == "2":
        send_issue("Water")

    elif choice == "3":
        send_issue("Internet")

    elif choice == "4":
        send_issue("Other")

    elif choice == "5":
        break

    else:
        print("Invalid button")