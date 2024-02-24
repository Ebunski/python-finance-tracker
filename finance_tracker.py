import datetime
import json

#Python array
transactions = [] 

# File handling
def load_data():
    """Loads data from transactions.json file."""
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []
    return transactions

def save_data(transactions):
    """Saves data to transactions.json file."""
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)


# Python functions
def add_transaction():
    """Adds a new transaction."""
    amount = float(input("Enter amount (positive for income, negative for expense): "))
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g: transport): ")
    transaction_type = input("Enter transaction type (income/expense): ").lower()
    if transaction_type not in ("income", "expense"):
        print("Invalid type. Please enter 'income' or 'expense'.")
        return

    transaction = {
        "amount": amount,
        "date": date,
        "category": category,
        "type": transaction_type
    }
    transactions.append(transaction)
    print(f"{transaction_type.capitalize()} added successfully!")
    save_data(transactions)

def show_balance():
    """Calculates and displays current balance."""
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expenses
    print(f"Your current balance is: {balance:.2f}")

def filter_transactions():
    """Filters transactions by date and displays them."""
    date = input("Enter date to filter (YYYY-MM-DD): ")
    filtered_transactions = [t for t in transactions if t["date"] == date]
    if filtered_transactions:
        print(f"Transactions for {date}:")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} - {transaction['type']}: {transaction['amount']:.2f} ({transaction['category']})")
    else:
        print("No transactions found for that date.")

def show_all_transactions():
    """Displays all transactions, sorted by date."""
    transactions.sort(key=lambda t: t["date"])
    print("All transactions (sorted by date):")
    for transaction in transactions:
        print(f"{transaction['date']} - {transaction['type']}: {transaction['amount']:.2f} ({transaction['category']})")

def calculate_days_between_transactions():
    """Calculates days between two transactions."""
    try:
        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")
        days_between = (datetime.datetime.strptime(date2, "%Y-%m-%d") - datetime.datetime.strptime(date1, "%Y-%m-%d")).days
        print(f"Days between transactions: {days_between}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    """Main menu for user interaction."""
    transactions = load_data()

    while True:
        print("\nFinance Tracker")
        print("1. Add transaction")
        print("2. View balance")
        print("3. Filter transactions")
        print("4. Show all transactions")
        print("5. Calculate days between transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_balance()
        elif choice == '3':
            filter_transactions()
        elif choice == '4':
            show_all_transactions()
        elif choice == '5':
            calculate_days_between_transactions()
        elif choice == '6':
            save_data(transactions)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
