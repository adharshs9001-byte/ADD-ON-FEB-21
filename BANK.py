class BankAccount:
    def __init__(self, holder_name, account_number, balance=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


# Example usage
account1 = BankAccount("Abhinav", "123456789", 1000)

account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)  # Example of insufficient balance
account1.display_balance()