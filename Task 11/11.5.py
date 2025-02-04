class BankAccount:

    def __init__(self, amount):
        # Making the amount attribute private
        self.__amount = amount

    # Getter method for amount
    def get_balance(self):
        return self.__amount

    # Setter method for deposit
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__amount += deposit_amount
        else:
            print("Deposit amount must be positive.")

    # Method for withdrawing with encapsulation
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            if withdraw_amount <= self.__amount:
                self.__amount -= withdraw_amount
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to check balance
    def check_balance(self):
        print("Balance:", self.__amount)


# Creating an account instance
account = BankAccount(1000)

# Depositing 500
account.deposit(500)

# Withdrawing 200
account.withdraw(200)

# Checking balance
account.check_balance()

# Attempting to access private attribute directly (will cause an error)
# print(account.__amount)  # Uncommenting this line will raise an AttributeError

# Using getter method to access balance
print("Accessing balance using getter:", account.get_balance())
