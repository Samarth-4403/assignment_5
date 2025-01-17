import random

class BankAccount:
    def __init__(self, name, initial_balance):
        self.account_number = self.generate_account_number()  # Generating a random account number
        self.name = name
        self.balance = initial_balance
        self.transactions = []  # List to store transaction logs
        self.min_balance = 0  # Minimum balance, default is 0
        self.transaction_limit = 5  # Limit of free transactions
        self.transaction_fee = 10  # Fee for transactions exceeding the limit

    @staticmethod
    def generate_account_number():
        return random.randint(1000000000, 9999999999)  # Generate a random 10-digit account number

    def add_log(self, transaction_type, amount):
        self.transactions.append({"type": transaction_type, "amount": amount})  # Log the transaction
        if len(self.transactions) > self.transaction_limit:
            self.balance -= self.transaction_fee  # Deduct transaction fee if limit exceeded
            self.transactions.append({"type": "transaction_fee", "amount": -self.transaction_fee})

    def withdraw(self, amount):
        if amount % 100 != 0:
            return "Withdrawal amount must be a multiple of 100."  # Check if amount is multiple of 100
        if amount > 10000:
            return "Withdrawal limit is 10000 per transaction."  # Check if amount exceeds the withdrawal limit
        if self.balance - amount < self.min_balance:
            return "Insufficient funds for withdrawal."  # Check if balance is sufficient

        self.balance -= amount
        self.add_log("withdraw", amount)
        return f"Withdrawn {amount}. New balance is {self.balance}."

    def deposit(self, amount):
        self.balance += amount
        self.add_log("deposit", amount)
        return f"Deposited {amount}. New balance is {self.balance}."

    def get_statement(self):
        return self.transactions[-10:]  # Return the last 10 transactions

    def get_account_info(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}  # Return account details

    def balance_enquiry(self):
        return self.balance  # Return current balance

class SavingsAccount(BankAccount):
    def __init__(self, name, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")  # Validate initial balance
        super().__init__(name, initial_balance)
        self.min_balance = 0  # Minimum balance for savings account

class CurrentAccount(BankAccount):
    def __init__(self, company_name, initial_balance):
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than 0.")  # Validate initial balance
        super().__init__(company_name, initial_balance)
        self.min_balance = 0  # Minimum balance for current account

def create_savings_account():
    name = input("Enter your name: ")  # Get user name
    initial_balance = get_initial_balance("Savings")
    return SavingsAccount(name, initial_balance)  # Create a savings account

def create_current_account():
    company_name = input("Enter your company name: ")  # Get company name
    initial_balance = get_initial_balance("Current")
    return CurrentAccount(company_name, initial_balance)  # Create a current account

def get_initial_balance(account_type):
    for _ in range(3):  # Allow up to 3 attempts for entering a valid initial balance
        try:
            initial_balance = float(input(f"Enter the initial balance for your {account_type} account: "))
            if initial_balance >= 0:
                return initial_balance  # Return initial balance if valid
        except ValueError:
            pass  # Ignore non-numeric input
        print("Initial balance must be a number greater than or equal to zero.")
    print("Too many invalid attempts. Exiting.")
    exit()  # Exit if too many invalid attempts

def main():
    print("Welcome to the Bank!")  # Greet the user
    account_type = input("Would you like to open a 'Savings' or 'Current' account? ").strip().lower()
    
    if account_type == "savings":
        account = create_savings_account()  # Create savings account
    elif account_type == "current":
        account = create_current_account()  # Create current account
    else:
        print("Invalid account type. Exiting.")
        return

    print(f"Account created successfully! Your account number is {account.account_number}.")
    
    while True:  # Infinite loop for user actions
        print("\nOptions: withdraw, deposit, statement, info, balance, exit")
        action = input("What would you like to do? ").strip().lower()
        
        if action == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))  # Handle withdrawal
        elif action == "deposit":
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))  # Handle deposit
        elif action == "statement":
            print(account.get_statement())  # Print statement
        elif action == "info":
            print(account.get_account_info())  # Print account info
        elif action == "balance":
            print(f"Your balance is {account.balance_enquiry()}.")  # Print balance enquiry
        elif action == "exit":
            print("Thank you for banking with us. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function if script is executed directly
