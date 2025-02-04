class BankAccount : 

    def __init__(self, amount) :
        self.amount = amount

    def deposit(self, deposit_amount) :
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount) :
        if withdraw_amount <= self.amount :
            self.amount -= withdraw_amount
        else :
            print("Insufficient balance")
    
    def check_balance(self) :
        print("Balance:", self.amount)


account = BankAccount(1000)

# depositing 500
account.deposit(500)

# withdrawing 200
account.withdraw(200)

# checking balance
account.check_balance()
