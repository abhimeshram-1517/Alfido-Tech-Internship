import requests

# External API URL

API_URL = "https://jsonplaceholder.typicode.com/users"

#API_URL = "https://jsonplaceholder.typicode.com/invalid-endpoint"


def fetch_users():
    """Fetch user data from the API."""

    try:
        print("=" * 50)
        print("       PYTHON API DATA FETCHER")
        print("=" * 50)

        print("\nConnecting to API...")

        # Send GET request
        response = requests.get(API_URL, timeout=10)

        # Check for HTTP errors
        response.raise_for_status()

        # Convert JSON response into Python data
        users = response.json()

        # Check response format
        if not isinstance(users, list):
            print("Error: Unexpected API response format.")
            return []

        print("\nAPI request successful!")
        print(f"Total users fetched: {len(users)}")

        return users

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request Error: {error}")

    except ValueError as error:
        print(f"JSON parsing error: {error}")

    return []


def display_users(users):
    """Display user information."""

    print("\n========== USER DETAILS ==========")

    for user in users:
        address = user.get("address") or {}
        company = user.get("company") or {}

        print("-" * 40)
        print("ID:", user.get("id", "N/A"))
        print("Name:", user.get("name", "N/A"))
        print("Username:", user.get("username", "N/A"))
        print("Email:", user.get("email", "N/A"))
        print("City:", address.get("city", "N/A"))
        print("Company:", company.get("name", "N/A"))


def search_users(users, search_term):
    """Search users by name, email, or city."""

    search_term = search_term.strip().casefold()

    if not search_term:
        print("Please enter a search term.")
        return

    results = []

    for user in users:
        address = user.get("address") or {}

        name = str(user.get("name", ""))
        email = str(user.get("email", ""))
        city = str(address.get("city", ""))

        if (
            search_term in name.casefold()
            or search_term in email.casefold()
            or search_term in city.casefold()
        ):
            results.append(user)

    print(f"\nSearch results for: {search_term}")

    if results:
        display_users(results)
        print(f"\nMatching users: {len(results)}")
    else:
        print("No matching users found.")


def main():
    """Main program."""

    users = fetch_users()

    if not users:
        print("\nNo user data available.")
        return

    while True:
        print("\n\n========== MENU ==========")
        print("1. Display all users")
        print("2. Search users")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_users(users)

        elif choice == "2":
            search_term = input(
                "Enter name, email, or city: "
            )
            search_users(users, search_term)

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()