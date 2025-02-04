class BankAccount:

    def __init__(self, amount):
        self.__amount = amount

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__amount += deposit_amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            if withdraw_amount <= self.__amount:
                self.__amount -= withdraw_amount
                print(f"Withdrew {withdraw_amount}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print("Balance:", self.__amount)

    def get_balance(self):
        return self.__amount


# Subclass demonstrating Method Overriding
class SavingsAccount(BankAccount):

    def __init__(self, amount, interest_rate):
        super().__init__(amount)
        self.interest_rate = interest_rate

    # Overriding the withdraw method to impose a withdrawal limit
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 5000:
            print("Cannot withdraw more than 5000 at once from a Savings Account.")
        else:
            super().withdraw(withdraw_amount)

    # New method to add interest to balance
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of {interest} added to the account.")


# Example Usage
if __name__ == "__main__":
    account = SavingsAccount(10000, 5)  # 5% interest rate

    # Depositing money
    account.deposit(2000)

    # Trying to withdraw more than the limit
    account.withdraw(6000)

    # Withdrawing within the limit
    account.withdraw(3000)

    # Adding interest
    account.add_interest()

    # Checking balance
    account.check_balance()
