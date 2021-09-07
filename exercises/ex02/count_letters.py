"""Counting letters in a string."""

__author__ = "730314539"

letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")
i: int = 0
count: int = 0

while i < len(word):
    if word[i] == letter:
        if count == 0:
            count = i + 1
    i = i + 1

output: str = str(count)

print("Count: " + output)