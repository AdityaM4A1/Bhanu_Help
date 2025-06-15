import os
FILE_NAME = "expenses.txt"
def load_expenses():
   expenses = []
   if os.path.exists(FILE_NAME):
       with open(FILE_NAME, "r") as file:
           lines = file.readlines()
           for line in lines[1:]:
               parts = line.strip().split('\t')
               if len(parts) == 2:
                   try:
                       expenses.append(float(parts[1]))
                   except ValueError:
                       print(f"Warning: Skipping invalid entry: {line.strip()}")
   return expenses
def save_expenses(expenses):
   with open(FILE_NAME, "w") as file:
       file.write("Day\tExpense\n")
       for i, amount in enumerate(expenses, start=1):
           file.write(f"{i}\t{amount:.2f}\n")
def add_expense(expenses):
   try:
       amount = float(input("Enter expense amount: "))
       expenses.append(amount)
       save_expenses(expenses)
       print("Expense added successfully.")
   except ValueError:
       print("Invalid input. Please enter a numeric value.")
def view_expenses(expenses):
   if not expenses:
       print("No expenses recorded yet.")
   else:
       print("Day\tExpense")
       for i, amount in enumerate(expenses, start=1):
           print(f"{i}\t{amount:.2f}")
def calculate_total(expenses):
   total = sum(expenses)
   print(f"Total expenses: {total:.2f}")

def calculate_average(expenses):
   if not expenses:
       print("No expenses to calculate average.")
   else:
       average = sum(expenses) / len(expenses)
       print(f"Average daily expense: {average:.2f}")

def main():
   expenses = load_expenses()
   while True:
       print("\nExpense Tracker Menu")
       print("1. Add Expense")
       print("2. View Expenses")
       print("3. Calculate Total Expenses")
       print("4. Calculate Average Expenses")
       print("5. Exit")
       choice = input("Enter your choice (1-5): ")
       if choice == "1":
           add_expense(expenses)
       elif choice == "2":
           view_expenses(expenses)
       elif choice == "3":
           calculate_total(expenses)
       elif choice == "4":
           calculate_average(expenses)
       elif choice == "5":
           print("Exiting application. Goodbye!")
           break
       else:
           print("Invalid choice. Please enter a number between 1 and 5.")
main()