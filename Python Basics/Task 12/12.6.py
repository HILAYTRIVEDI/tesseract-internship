class NegativeDepositError(Exception):
    def __init__(self, amount, message="Cannot deposit a negative amount!"):
        self.amount = amount
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError(amount)
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def main():
    account = BankAccount(1000)

    try:
        account.deposit(500)
        account.deposit(-200)
    except NegativeDepositError as e:
        print(f"Error: Tried to deposit {e.amount}. {e.message}")

    try:
        account.withdraw(2000)
    except ValueError as e:
        print(f"Error: {e}")

    # Check the final balance
    account.check_balance()

if __name__ == "__main__":
    main()
