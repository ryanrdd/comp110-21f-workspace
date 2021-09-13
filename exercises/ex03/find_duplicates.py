"""Finding duplicate letters in a word."""

__author__ = "730314539"

word: str = input("Enter a word: ")

i: int = 0
j: int = 0
count: bool = False

while i < len(word):
    while j < len(word):
        print("i" + str(i))
        print("j" + str(j))
        if i != j:
            if word[i] == word[j]:
                count = True
        j = j + 1
    i = i + 1

print("Found duplicate: " + str(count))