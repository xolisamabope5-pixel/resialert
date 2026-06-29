# =========================
# RESIALERT SYSTEM (PHASE 3 + SAVE VERSION)
# =========================

def save_complaint(text):
    with open("complaints.txt", "a") as file:
        file.write(text + "\n\n")


print("=" * 35)
print("           RESIALERT")
print("=" * 35)

while True:

    print("\nSelect an issue to report:")
    print("1. Electricity Issue")
    print("2. Water Issue")
    print("3. Internet Issue")
    print("4. Other Issue")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        room = input("Enter your room number: ")

        report = f"""
RESIALERT COMPLAINT
-------------------
Issue: Electricity
Room: {room}
Status: Submitted
"""

        print(report)
        save_complaint(report)

    elif choice == "2":
        room = input("Enter your room number: ")

        report = f"""
RESIALERT COMPLAINT
-------------------
Issue: Water
Room: {room}
Status: Submitted
"""

        print(report)
        save_complaint(report)

    elif choice == "3":
        room = input("Enter your room number: ")

        report = f"""
RESIALERT COMPLAINT
-------------------
Issue: Internet
Room: {room}
Status: Submitted
"""

        print(report)
        save_complaint(report)

    elif choice == "4":
        room = input("Enter your room number: ")
        problem = input("Describe the issue: ")

        report = f"""
RESIALERT COMPLAINT
-------------------
Issue: Other
Room: {room}
Details: {problem}
Status: Submitted
"""

        print(report)
        save_complaint(report)

    elif choice == "5":
        print("Exiting ResiAlert. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")