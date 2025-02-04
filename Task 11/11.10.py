class BankAccount:
    def __init__(self, amount):
        # Private attribute to store the balance
        self.__balance = amount

    # Getter method to access balance using @property
    @property
    def balance(self):
        print("Getting balance...")
        return self.__balance

    # Setter method to modify balance safely
    @balance.setter
    def balance(self, new_amount):
        if new_amount < 0:
            print("Balance cannot be negative!")
        else:
            print(f"Setting balance to {new_amount}...")
            self.__balance = new_amount

    # Deleter method to delete balance if needed
    @balance.deleter
    def balance(self):
        print("Deleting balance...")
        del self.__balance


# Example Usage
if __name__ == "__main__":
    # Creating a bank account with an initial balance
    account = BankAccount(1000)

    # Accessing balance using the getter
    print(account.balance)  # Output: Getting balance... 1000

    # Modifying balance using the setter
    account.balance = 2000  # Output: Setting balance to 2000...

    # Checking the updated balance
    print(account.balance)  # Output: Getting balance... 2000

    # Trying to set a negative balance
    account.balance = -500  # Output: Balance cannot be negative!

    # Deleting the balance attribute
    del account.balance  # Output: Deleting balance...

    # Trying to access balance after deletion (will raise an error)
    try:
        print(account.balance)
    except AttributeError as e:
        print(f"Error: {e}")
