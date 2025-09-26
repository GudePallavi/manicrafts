import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Ensure CSV file has headers if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])

# Add a new expense
def add_expense():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])
    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n📌 All Expenses:")
        for row in reader:
            print(row)

# Search expenses by category
def search_by_category():
    category = input("Enter category to search: ")
    total = 0
    print(f"\n🔍 Expenses in category: {category}")
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Category"].lower() == category.lower():
                print(row)
                total += float(row["Amount"])
    print(f"💰 Total spent in {category}: {total}\n")

# View total spent per category
def total_per_category():
    totals = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            totals[category] = totals.get(category, 0) + float(row["Amount"])

    print("\n📊 Total spent per category:")
    for category, total in totals.items():
        print(f"{category}: {total}")

# View monthly total spending
def monthly_spending():
    month = input("Enter month (YYYY-MM): ")
    total = 0
    print(f"\n📆 Expenses in {month}:")
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                print(row)
                total += float(row["Amount"])
    print(f"💰 Total spent in {month}: {total}\n")

# CLI Menu
def menu():
    initialize_file()
    while True:
        print("\n====== Expense Tracker 2.0 ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Total Spent per Category")
        print("5. Monthly Spending")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            total_per_category()
        elif choice == "5":
            monthly_spending()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    menu()
