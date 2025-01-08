# Q3 Create a simple expense tracker where users can add, view, and delete expenses.


class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, category, amount, description):
        """Add a new expense."""
        expense_id = len(self.expenses) + 1
        self.expenses[expense_id] = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        print(f"Expense added successfully. ID: {expense_id}")

    def view_expenses(self):
        """View all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for expense_id, expense in self.expenses.items():
                print(f"ID: {expense_id}")
                print(f"Date: {expense['date']}")
                print(f"Category: {expense['category']}")
                print(f"Amount: {expense['amount']}")
                print(f"Description: {expense['description']}\n")

    def delete_expense(self, expense_id):
        """Delete an expense by ID."""
        if expense_id in self.expenses:
            del self.expenses[expense_id]
            print(f"Expense {expense_id} deleted successfully.")
        else:
            print(f"Expense {expense_id} not found.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            tracker.add_expense(date, category, amount, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            tracker.delete_expense(expense_id)
        elif choice == "4":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

