"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(e_list: list[int]) -> list[int]:
    """A function that returns only even values."""
    i: int = 0
    p: list[int] = []
    if len(e_list) >= 1:
        while i < len(e_list):
            n_1: int = e_list[i]
            if n_1 % 2 == 0:
                p.append(n_1)
            i += 1

    return p


def sub(s_list: list[int], start: int, end: int) -> list[int]:
    """Returns a list which is a subset of a given list with start and end points."""
    i: int = 0
    n: list[int] = []
    if len(s_list) >= 1:
        while i < len(s_list):
            if i >= start and i <= (end - 1):
                n.append(s_list[i])
            i += 1

    return n


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Returns a new list with a_list and b_list."""
    new: list[int] = []
    new = a_list + b_list
    return new