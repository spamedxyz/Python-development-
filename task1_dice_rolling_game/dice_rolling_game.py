"""Task 1: Dice Rolling Game.

Simulates rolling two dice and asks the user whether to roll again.
"""

from __future__ import annotations

import random


def roll_dice() -> tuple[int, int]:
    """Return two random dice values between 1 and 6."""
    return random.randint(1, 6), random.randint(1, 6)


def score_roll(die_one: int, die_two: int) -> tuple[int, str]:
    """Return points and a short message for the current roll."""
    total = die_one + die_two
    if die_one == die_two:
        return 5, "Double roll! You earned 5 points."
    if total >= 10:
        return 3, "Great roll! You earned 3 points."
    if total >= 7:
        return 2, "Good roll! You earned 2 points."
    return 1, "Better luck next time. You earned 1 point."


def main() -> None:
    """Run the interactive dice rolling game."""
    score = 0
    print("=" * 42)
    print("Dice Rolling Game")
    print("=" * 42)

    while True:
        input("\nPress Enter to roll the dice...")
        die_one, die_two = roll_dice()
        points, message = score_roll(die_one, die_two)
        score += points

        print(f"\nDie 1: {die_one}")
        print(f"Die 2: {die_two}")
        print(f"Total: {die_one + die_two}")
        print(message)
        print(f"Current score: {score}")

        choice = input("\nRoll again? (y/n): ").strip().lower()
        if choice != "y":
            break

    print("\nGame over.")
    print(f"Final score: {score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
