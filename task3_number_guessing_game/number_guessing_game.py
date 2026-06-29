"""Task 3: Number Guessing Game.

The computer selects a number between 1 and 100 and gives hints until the
player guesses correctly or runs out of attempts.
"""

from __future__ import annotations

import random


def check_guess(guess: int, secret_number: int) -> str:
    """Return feedback for a guess."""
    if guess == secret_number:
        return "correct"
    if guess < secret_number:
        return "low"
    return "high"


def play_round(max_attempts: int = 7) -> None:
    """Play one round of the number guessing game."""
    secret_number = random.randint(1, 100)
    attempts_left = max_attempts

    print("\nI am thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")

    while attempts_left > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        result = check_guess(guess, secret_number)
        if result == "correct":
            used_attempts = max_attempts - attempts_left + 1
            print(f"Congratulations! You guessed it in {used_attempts} attempts.")
            return

        attempts_left -= 1
        if result == "low":
            print("Too low.")
        else:
            print("Too high.")
        print(f"Attempts left: {attempts_left}")

    print(f"\nGame over. The correct number was {secret_number}.")


def main() -> None:
    """Run the interactive number guessing game."""
    print("=" * 42)
    print("Number Guessing Game")
    print("=" * 42)

    while True:
        play_round()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
