"""exercises.ex01.relational_operators!"""

__author__ = "730314539"

number_1: str = (input("Left-hand side: "))
n2: str = (input("Right-hand side: "))

int_1: int = int(number_1)
int_2: int = int(n2)

less_int: bool = (int_1 < int_2)
greater_equal_int: bool = (int_1 >= int_2)
equal_int: bool = (int_1 == int_2)
not_equal_int: bool = (int_1 != int_2)

print(number_1 + " < " + n2 + " is " + str(less_int))
print(number_1 + " >= " + n2 + " is " + str(greater_equal_int))
print(number_1 + " == " + n2 + " is " + str(equal_int))
print(number_1 + " != " + n2 + " is " + str(not_equal_int))