expenses = []

def welcome():
    print("Welcome to the app")
def thanks():
      print("Thank you for using the expense tracker !")
def expense_log():
    while True:
        try:
            amount = float(input("What is the amount? "))
            if amount <= 0:
                raise ValueError("Please enter an amount over 0...")
            break
        except ValueError as x:
            print("Error: ", x)

    category = input("What is the category? (Food, Transport, Entertainment): ")
    description = input("What is the description? ")
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print(expenses)


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print("Total amount of expenses: ", total)

def show_category_total():
      category_totals = {}
      
      for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_totals:
                  category_totals[category] += amount
            else:
                category_totals[category] = amount
      for category, total in category_totals.items():
            print("Total for ", category, ": ", total)  


def main():
    welcome()

    while True:
        expense_log()
        choice = input("Would you like to add another expense? (yes/no) ")
        if choice == "no":
            break

    choice2 = input("What would you like to do ? 1: Show sum of all amounts 2: Show total in each category 3: Show a list of all expenses with their details? 4: Exit the app")
    if choice2 == "1":
                show_total()
    elif choice2 == "2":
                show_category_total()
    elif choice2 == "3":
                print(expenses)
    elif choice == "4":
          thanks()
    thanks()


if __name__ == "__main__":
    main()