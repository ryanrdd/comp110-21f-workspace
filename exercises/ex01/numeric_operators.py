"""exercises.ex01.numeric_operators!"""

__author__ = "730314539"

input_1: str = (input("Left-hand side: "))
input_2: str = (input("Right-hand side: "))

int_1: int = int(input_1)
int_2: int = int(input_2)

square_int: int = (int_1**int_2)
divide_int: float = (int_1 / int_2)
integer_int: int = (int_1 // int_2)
modulo_int: int = (int_1 % int_2)

print(input_1 + " ** " + input_2 + " is " + str(square_int))
print(input_1 + " / " + input_2 + " is " + str(divide_int))
print(input_1 + " // " + input_2 + " is " + str(integer_int))
print(input_1 + " % " + input_2 + " is " + str(modulo_int))