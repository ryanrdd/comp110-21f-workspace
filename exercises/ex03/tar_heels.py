"""An exercise in remainders and boolean logic."""

__author__ = "730314539"

guess: str = input("Enter an int: ")
both: int = 0

if int(guess) % 2 == 0:
    both = 1 + both
if int(guess) % 7 == 0:
    both = 2 + both
if both == 3:
    print("TAR HEELS")
if both == 2:
    print("HEELS")
if both == 1:
    print("TAR")
if both == 0:
    print("CAROLINA")