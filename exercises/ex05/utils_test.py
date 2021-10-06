"""Unit tests for list utility functions."""

__author__ = "730314539"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_1():
    """Tests to see if only evens are captured in a list, regular case"""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_2():
    """Tests to see if only evens are captured in a list, the zero case."""
    xs: list[int] = [0, 1, 4, 5]
    assert only_evens(xs) == [0, 4]


def test_only_evens_3():
    """Tests to see if only evens are captured in a list, the negative case or edge case."""
    xs: list[int] = [-2, 3, 5]
    assert only_evens(xs) == [-2]


def test_sub_1():
    "Tests to see if original list is changed into list containing start and end points."
    assert sub([1, 2, 3, 4, 5], 1, 3) == [2, 3]


def test_sub_2():
    "Tests to see if original list is changed into list containing start and end points."
    assert sub([1, 2, 3, 4, 5], -1, 5) == [1, 2, 3, 4, 5]


def test_sub_3():
    "Tests to see if original list is changed into list containing start and end points."
    assert sub([1, 2, 3], 0, 100) == [1, 2, 3]


def test_concat_1():
    """Tests to see if lists are added to each other without changing order."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]


def test_concat_2():
    """Tests to see if lists are added to each other without changing order."""
    assert concat([72, 12, 0], [11, 0, 0]) == [72, 12, 0, 11, 0, 0]


def test_concat_3():
    """Tests to see if lists are added to each other without changing order."""
    assert concat([], [1]) == [1]