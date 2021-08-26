"""numeric_operators EX01 RYANRD"""

__author__ = "730314539"

n1: str = (input("Left-hand side: "))
n2: str = (input("Right-hand side: "))

intn1: int = int(n1)
intn2: int = int(n2)

squareint: int = (intn1**intn2)
devint: float = (intn1 / intn2)
inteint: int = (intn1 // intn2)
remaint: int = (intn1 % intn2)

print(n1 + " ** " + n2 + " is " + str(squareint))
print(n1 + " / " + n2 + " is " + str(devint))
print(n1 + " // " + n2 + " is " + str(inteint))
print(n1 + " % " + n2 + " is " + str(remaint))