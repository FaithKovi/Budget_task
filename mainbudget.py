
database = {"Wach": 200, "Kaka": 2000, "Obinna": 7000, "Gigi": 1000}

class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.current_balance = 50000

    def deposit_operation(self, database):
        self.current_balance += self.amount
        global budget_name
        database[budget_name] = self.current_balance
        print(f"\nYou have ${self.current_balance} in your {self.category} category\n")

    def withdraw_operation(self, balance):
        self.current_balance = balance
        if (self.amount > (self.current_balance - 1)):
            print(f"\nInsufficient funds in {self.category} category \n") 
        elif (self.amount <= (self.current_balance - 1)):
            self.current_balance -= self.amount
            print (f"\nYou have ${self.current_balance} in your {self.category}\n")
        else:
            print("\nInvalid selection, try again\n")
            withdraw_operation(self)

    def check_balance(self):
        self.current_balance = self.amount
        print(f"Your current balnce for {self.category} category is ${self.current_balance}")

            

    def transfer_funds(self, transfer_amount, new_amount):
        self.current_balance = self.amount
        self.amount = transfer_amount
        for from_name, from_amount in database.items():
            if (from_amount == self.current_balance):
                if self.amount < (self.current_balance - 1):
                    database[from_name] -= self.amount
                    for to_name, to_amount in database.items():
                        if (to_amount == new_amount):
                            database[to_name] += self.amount
                            print(f"\n${self.amount} has been transferred to {to_name} budget\n")
                            print(f"The current balance in {to_name} is ${database[to_name]}\n")
                    print(f"\n${self.amount} has been transferred from {from_name} budget\n")
                    print(f"The current balance in {from_name} is ${database[from_name]}\n")
                else:
                    print(f"Insufficient balance in {from_name} budget!")


def init():
    print ("====Welcome to the budget App====\n")
    global choice
    choice = int(input("Which category would you like to budget for? \n Press 1 - Food \n Press 2 - Clothing \n Press 3 - Entertainment\n"))
    global category
    if choice == 1:
        category = "Food"
        return category
    elif choice == 2:
        category = "Clothing"
        return category
    elif choice == 3:
        category = "Entertainment"
        return category
    else:
        print("Pick a valid option")


init()


def new_budget():
    print("=======Creating a New Budget=======\n")

    global budget_name
    budget_name = input("Enter budget name: \n")
    global budget_amount
    budget_amount = int(input("How much would you like to deposit? \n$"))
    database[budget_name] = budget_amount
    print(f"{budget_name} budget was setup with ${budget_amount}")
    return budget_amount


def withdraw_budget():
    print("=======Withdraw a Budget=======\n")

    global budget_name
    budget_name = input("Enter budget name: \n")
    for check_budget in database.keys():
        if (check_budget == budget_name):
            global budget_amount_withdraw
            budget_amount_withdraw = int(input("How much would you like to withdraw? \n$"))
            global balance
            balance = database[budget_name]
            return budget_amount_withdraw, balance
            

def check_budget():
    print("=======Check Budget Balance=======\n")

    global budget_name
    budget_name = input("Enter budget name: \n")
    for check_budget in database.keys():
        if (check_budget == budget_name):
            global budget_balance
            budget_balance = database[budget_name]
            return budget_balance


def tranfer_budget():
    print("=======Transfer a Budget Amount=======\n")

    # transfer from
    def from_budget():
        global from_budget_name
        from_budget_name = input("Enter budget name you wish to transfer from: \n")
        for collect_case_name in database.keys():
            if (from_budget_name == collect_case_name):
                global collect_case_amount
                collect_case_amount = database[from_budget_name]
                global amount_to_transfer
                amount_to_transfer = int(input("Enter the amount to transfer: $"))
                return collect_case_amount, amount_to_transfer
        
    #transfer to
    def to_budget():
        global to_budget_name
        to_budget_name = input("Enter budget name you wish to transfer to: \n")
        for transfer_case_name, transfer_case_amount in database.items():
            if (transfer_case_name == to_budget_name):
                transfer_case_amount = database[to_budget_name]
                return transfer_case_amount


    global transfer_data
    transfer_data = from_budget()
    global receive_data
    receive_data = to_budget()
    
    return transfer_data[0], transfer_data[1], receive_data


def main_operation():
    global category
    operation = int(input("What would you like to do? \n Press 1 - Deposit \n Press 2 - Withdraw \n Press 3 - Check balance \n Press 4 - Transfer funds to another category \n"))
    if operation == 1:
        deposit_amount = new_budget()
        budget = Budget(category, deposit_amount)
        budget.deposit_operation(database)
    elif operation == 2:
        [withdraw_amount, balance] = withdraw_budget()
        budget = Budget(category, withdraw_amount)
        budget.withdraw_operation(balance)
    elif operation == 3:
        check_balance = check_budget()
        budget = Budget(category, check_balance)
        budget.check_balance()
    elif operation == 4:
        [current_transfer_balance, transfer_amount, to_funds] = tranfer_budget()
        budget = Budget(category, current_transfer_balance)
        budget.transfer_funds(transfer_amount, to_funds)
    else:
        print("Invalid option")

main_operation()

def rating():
    print("\nHope you had a good experience\n")
    rating = input("\nRate your experience on this app: \n Press 1 - * \n Press 2 - ** \n Press 3 - *** \n Press 4 - **** \n Press 5 - ***** \n press Enter to skip1\n")

    if rating == "1":
        print("*")
    elif rating == "2":
        print("**")
    elif rating == "3":
        print("***")
    elif rating == "4":
        print("****")   
    elif rating == "5":
        print("*****")
    elif rating == "":
        quit()
    else:
        print("Invalid selection")
        rating()
    
rating()

