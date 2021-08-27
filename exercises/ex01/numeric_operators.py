"""exercises.ex01.numeric_operators!"""

__author__ = "730314539"

input1: str = (input("Left-hand side: "))
input2: str = (input("Right-hand side: "))

int1: int = int(input1)
int2: int = int(input2)

square_int: int = (int1**int2)
divide_int: float = (int1 / int2)
integer_int: int = (int1 // int2)
modulo_int: int = (int1 % int2)

print(input1 + " ** " + input2 + " is " + str(square_int))
print(input1 + " / " + input2 + " is " + str(divide_int))
print(input1 + " // " + input2 + " is " + str(integer_int))
print(input1 + " % " + input2 + " is " + str(modulo_int))