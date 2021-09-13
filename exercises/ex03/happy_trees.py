"""Drawing forests in a loop."""

__author__ = "730314539"

TREE: str = '\U0001F332'

enter: str = input("Depth: ")
depth: int = 0
output: int = 0

while depth < int(enter):
    if output <= depth:
        print(str(TREE * (output + 1)))
        output = output + 1
    depth = depth + 1