class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Add amount to balance
        self.account_balance += amount

    def withdraw(self, amount):
        # Withdraw only if sufficient funds
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Print balance in user-friendly format
        print(f"Current Balance: ${self.account_balance}")

