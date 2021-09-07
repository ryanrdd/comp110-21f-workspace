"""Repeating a beat in a loop."""

__author__ = "730314539"

name: str = input("What beat do you want to repeat? ")
times: str = input("How many times do you want to repeat it? ")
counter: int = int(times)
output: str = str()

if counter <= 0:
    print("No beat...")
else:
    while counter > 0:
        output = output + name
        if counter != 1:
            output = output + " "
        counter = counter - 1

print(output)