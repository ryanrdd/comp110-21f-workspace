"""exercises.ex01.relational_operators!"""

__author__ = "730314539"

n1: str = (input("Left-hand side: "))
n2: str = (input("Right-hand side: "))

intn1: int = int(n1)
intn2: int = int(n2)

lessint: bool = (intn1 < intn2)
greateqint: bool = (intn1 >= intn2)
eqint: bool = (intn1 == intn2)
noteqint: bool = (intn1 != intn2)

print(n1 + " < " + n2 + " is " + str(lessint))
print(n1 + " >= " + n2 + " is " + str(greateqint))
print(n1 + " == " + n2 + " is " + str(eqint))
print(n1 + " != " + n2 + " is " + str(noteqint))