from models import User
from utils import get_user, create_user, update_user, delete_user


while True:

    print("\n===== USER MANAGER =====")
    print("1. Get user")
    print("2. Create user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")

    
    choice = input("Choose an option: ").strip()

    # ---------------- GET USER ----------------
    if choice == "1":

        try:
            user_id = int(input("Enter user ID: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        data = get_user(user_id)

        if data:
            user = User(
                data["name"],
                data["email"],
                data["address"]["city"]
            )

            user.show_info()

        else:
            print("User not found.")

    # ---------------- CREATE USER ----------------
    elif choice == "2":

        name = input("Enter name: ")
        email = input("Enter email: ")
        city = input("Enter city: ")

        if not name.strip() or not email.strip() or not city.strip():
            print("Name, email, and city cannot be empty.")
            continue

        if "@" not in email or "." not in email:
            print("Please enter a valid email.")
            continue

        response = create_user(name, email, city)

        print("Status:", response.status_code)

        if response.status_code == 201:
            print("User created successfully!")
            print(response.json())

        else:
            print("Failed to create user.")

    # ---------------- UPDATE USER ----------------
    elif choice == "3":

        try:
            user_id = int(input("Enter user ID to update: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        name = input("Enter new name: ")
        email = input("Enter new email: ")
        city = input("Enter new city: ")

        response = update_user(user_id, name, email, city)

        print("Status:", response.status_code)

        if response.status_code == 200:
            print("User updated successfully!")
            print(response.json())

        else:
            print("Failed to update user.")

    # ---------------- DELETE USER ----------------
    elif choice == "4":

        try:
            user_id = int(input("Enter user ID to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        response = delete_user(user_id)

        print("Status:", response.status_code)

        if response.status_code == 200:
            print("User deleted successfully!")

        else:
            print("Failed to delete user.")

    # ---------------- EXIT ----------------
    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid option. Please choose 1-5.")