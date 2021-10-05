"""Unit tests for list utility functions."""

__author__ = "730314539"


from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens():
    """Tests to see if only evens are captured in a list."""
    assert only_evens([1, 2, 3]) == [2]
    assert only_evens([0, 1, 4, 5]) == [0, 4]
    assert only_evens([-2, 3, 5]) == [-2]


def test_sub():
    "Tests to see if original list is changed into list containing start and end points."
    assert sub([1, 2, 3, 4, 5], 1, 3) == [2, 3]
    assert sub([1, 2, 3, 4, 5], -1, 5) == [1, 2, 3, 4, 5]
    assert sub([1, 2, 3], 0, 100) == [1, 2, 3]


def test_concat():
    """Tests to see if lists are added to each other without changing order."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]
    assert concat([72, 12, 0], [11, 0, 0]) == [72, 12, 0, 11, 0, 0]
    assert concat([], [1]) == [1]