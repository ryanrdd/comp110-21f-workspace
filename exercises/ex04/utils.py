"""List utility functions."""

__author__ = "730314539"


def all(sequence: list[int], number: int) -> bool:
    """all list implementation"""
    i: int = 0
    if len(sequence) >= 1:
        while i < len(sequence):
            item: int = sequence[i]
            if item != number:
                return False
            i += 1
    else:
        return False

    return True


def is_equal(l_1: list[int], l_2: list[int]) -> bool:
    """is_equal list boolean"""
    f: int = 0
    if len(l_1) != len(l_2):
        return False   
    else:
        while f < len(l_1):
            if l_1[f] != l_2[f]:
                return False
            f = f + 1

    return True

def max(input: list[int]) -> int:
    """Maximum Value in a list of integers"""
    k: int = 0
    value: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while k < len(input):
            if value < input[k]:
                value = input[k]
            k += 1

    return value