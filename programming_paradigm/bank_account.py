class BankAccount:
    """
    A class to represent a simple Bank Account.
    Encapsulates account balance and provides methods for banking operations.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance.
        """
        # Encapsulation: Using a protected attribute for the balance
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount if funds are sufficient.
        Returns True on successful withdrawal, False otherwise.
        """
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False # Insufficient funds or invalid amount

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Note: The expected output format is "Current Balance: ${amount}"
        print(f"Current Balance: ${self._account_balance:.2f}")

# Note: No need for a main block in this file since main-0.py handles execution