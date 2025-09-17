import csv
import os

FILENAME = "expenses.csv"

# --- Utility Functions ---
def init_file():
    """Create the CSV file if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])  # Header row


def add_expense(description, amount):
    """Add a new expense to the CSV file."""
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])


def view_expenses():
    """Read and display all expenses."""
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n--- All Expenses ---")
        for row in reader:
            print(f"{row[0]} - ₹{row[1]}")


def total_spent():
    """Calculate and display the total amount spent."""
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[1])
    print(f"\n💰 Total Spent: ₹{total}")


# --- CLI Menu ---
def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(desc, amount)
            print("✅ Expense Added!")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    init_file()
    menu()
