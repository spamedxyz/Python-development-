"""Task 4: ATM Simulation.

Demonstrates a simple ATM system using Object-Oriented Programming.
Users can check balance, deposit money, and withdraw funds.
"""

from __future__ import annotations


class ATMAccount:
    """Encapsulates account balance and banking operations."""

    def __init__(self, starting_balance: float = 0.0) -> None:
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self._balance = float(starting_balance)

    @property
    def balance(self) -> float:
        """Return the current account balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Deposit a positive amount."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw a positive amount if enough balance is available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


class ATMController:
    """Handles user interaction for the ATM account."""

    def __init__(self, account: ATMAccount) -> None:
        self.account = account

    @staticmethod
    def read_amount(prompt: str) -> float | None:
        """Read a money amount and handle invalid input."""
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            return None

    def show_balance(self) -> None:
        """Display current balance."""
        print("\n" + "*" * 30)
        print(f"Current Balance: ${self.account.balance:.2f}")
        print("*" * 30)

    def run(self) -> None:
        """Run the ATM menu loop."""
        while True:
            print("\n" + "=" * 35)
            print("ATM Simulation")
            print("=" * 35)
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                self.show_balance()

            elif choice == "2":
                amount = self.read_amount("Enter amount to deposit: $")
                if amount is not None:
                    try:
                        self.account.deposit(amount)
                        print(f"${amount:.2f} deposited successfully.")
                    except ValueError as error:
                        print(error)

            elif choice == "3":
                amount = self.read_amount("Enter amount to withdraw: $")
                if amount is not None:
                    try:
                        self.account.withdraw(amount)
                        print(f"${amount:.2f} withdrawn successfully.")
                    except ValueError as error:
                        print(error)

            elif choice == "4":
                print("\nThank you for using the ATM Simulation.")
                print(f"Final Balance: ${self.account.balance:.2f}")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 4.")


def main() -> None:
    """Create an account and start the ATM controller."""
    account = ATMAccount(starting_balance=0.0)
    ATMController(account).run()


if __name__ == "__main__":
    main()
