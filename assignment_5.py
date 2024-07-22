import random

class Account:
  def __init__(self, account_type, name, initial_balance=0):
    self.account_type = account_type
    self.name = name
    self.balance = initial_balance
    self.min_balance = 0  # Savings account can have 0 minimum balance
    self.account_number = self.generate_account_number()
    self.transactions = []
    self.transaction_limit = 5
    self.transaction_fee = 10

  def generate_account_number(self):
    return random.randint(100000, 999999)

  def add_log(self, message):
    self.transactions.append(message)
    if len(self.transactions) > self.transaction_limit:
      self.transactions.pop(0)  # Remove oldest transaction if limit reached
      self.balance -= self.transaction_fee
      self.add_log(f"Transaction fee of Rs.{self.transaction_fee} applied for exceeding limit")

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      self.add_log(f"Deposited Rs.{amount}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if amount % 100 != 0:
      print("Withdrawal amount must be a multiple of Rs.100")
    elif amount > 10000:
      print("Withdrawal limit exceeded. Maximum withdrawal per transaction is Rs.10000")
    elif amount > self.balance:
      print("Insufficient funds")
    else:
      self.balance -= amount
      self.add_log(f"Withdrew Rs.{amount}")

  def get_statement(self):
    print(f"Account Statement for {self.name} ({self.account_number})")
    for transaction in self.transactions:
      print(transaction)
    print(f"Current Balance: Rs.{self.balance}")

  def get_account_info(self):
    print(f"Account Information:")
    print(f"Account Type: {self.account_type}")
    print(f"Account Holder: {self.name}")
    print(f"Account Number: {self.account_number}")
    print(f"Minimum Balance: Rs.{self.min_balance}")
    print(f"Current Balance: Rs.{self.balance}")

  def balance_enquiry(self):
    print(f"Your current balance is Rs.{self.balance}")


def create_account():
  account_type = input("Enter account type (Savings/Current): ")
  name = input("Enter your name: ")

  if account_type.lower() == "savings":
    initial_balance = 0  # Default for savings account
  else:
    # Validate initial balance for current account
    for i in range(3):
      initial_balance = float(input("Enter initial balance (must be greater than Rs.0): "))
      if initial_balance > 0:
        break
      else:
        print("Invalid initial balance. Please enter a value greater than Rs.0")
    if initial_balance <= 0:
      print("Failed to create account. Minimum initial balance not met.")
      return

  account = Account(account_type, name, initial_balance)
  print(f"Account created successfully!\nYour account number is: {account.account_number}")
  return account


def main():
  print("Welcome to the Bank Management System")
  account = None

  while True:
    print("\nMenu:")
    print("1. Create Account")
    print("2. View Account Information")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Get Mini Statement")
    print("6. Balance Enquiry")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      account = create_account()
    elif choice == "2" and account:
      account.get_account_info()
    elif choice == "3" and account:
      amount = float(input("Enter amount to deposit: "))
      account.deposit(amount)
    elif choice == "4" and account:
      amount = float(input("Enter amount to withdraw: "))
      if amount % 100 != 0:
        print("Withdrawl amount must be a multiple of Rs 100")
      elif amount > 10000:
        print("Withdrawal limit exceeded. Maximum withdrawal per transaction is Rs.10000")
      elif amount > self.balance:
        print("Insufficient funds")
      else:
        # Check transaction limit and apply fee if exceeded
        if len(account.transactions) >= account.transaction_limit:
            print(f"Transaction limit of {account.transaction_limit} reached. A fee of Rs.{account.transaction_fee} will be applied.")
            account.balance -= account.transaction_fee  # Deduct fee before withdrawal
            account.add_log(f"Transaction fee of Rs.{account.transaction_fee} applied for exceeding limit")
        account.withdraw(amount)