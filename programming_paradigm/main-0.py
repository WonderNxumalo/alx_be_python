import sys
from bank_account import BankAccount

def main():
    # Initialize the account with a starting balance of 100 as per example
    account = BankAccount(100)

    # Check for minimum arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount from the second argument
    # Example sys.argv[1] would be "deposit:50" or "withdraw:20" or just "display"
    parts = sys.argv[1].split(':')
    command = parts[0]
    
    # Check if a parameter (amount) was provided and convert it to a float
    params = parts[1:]
    amount = float(params[0]) if params else None

    # --- Operation Logic ---

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        # Expected Output: Deposited: $50
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            # Expected Output: Withdrew: $20
            print(f"Withdrew: ${amount}")
        else:
            # Expected Output: Insufficient funds.
            print("Insufficient funds.")

    elif command == "display":
        # Expected Output: Current Balance: ${amount}
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()