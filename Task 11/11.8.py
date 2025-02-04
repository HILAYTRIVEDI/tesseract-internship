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


class SavingsAccount(BankAccount):

    def __init__(self, amount, interest_rate):
        super().__init__(amount)
        self.interest_rate = interest_rate

    def withdraw(self, withdraw_amount):
        if withdraw_amount > 5000:
            print("Cannot withdraw more than 5000 at once from a Savings Account.")
        else:
            super().withdraw(withdraw_amount)

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of {interest} added to the account.")


class LoanAccount:

    def __init__(self, loan_amount):
        self.loan_amount = loan_amount

    def get_loan_balance(self):
        print(f"Outstanding Loan Balance: {self.loan_amount}")

    def make_loan_payment(self, payment_amount):
        if payment_amount > 0:
            if payment_amount <= self.loan_amount:
                self.loan_amount -= payment_amount
                print(f"Loan payment of {payment_amount} made.")
            else:
                print("Payment exceeds loan balance.")
        else:
            print("Payment amount must be positive.")


# Multiple Inheritance
class PremiumAccount(SavingsAccount, LoanAccount):

    def __init__(self, amount, interest_rate, loan_amount):
        SavingsAccount.__init__(self, amount, interest_rate)
        LoanAccount.__init__(self, loan_amount)

    # Additional feature for premium accounts
    def request_loan_extension(self):
        print("Loan extension request submitted.")


# Example Usage
if __name__ == "__main__":
    premium = PremiumAccount(20000, 4, 50000)  # 4% interest rate, 50000 loan balance

    # Depositing money
    premium.deposit(5000)

    # Withdrawing within the limit
    premium.withdraw(3000)

    # Adding interest
    premium.add_interest()

    # Checking balance
    premium.check_balance()

    # Checking loan balance
    premium.get_loan_balance()

    # Making loan payment
    premium.make_loan_payment(10000)

    # Requesting loan extension
    premium.request_loan_extension()
