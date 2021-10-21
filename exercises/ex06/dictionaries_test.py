"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert

__author__ = "730314539"

def test_invert_1():
    """Tests to see if a sample list gets inverted."""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_2():
    """Tests to see if the list returns KeyError."""
    assert invert({'never': '1', 'copy': '2', 'always': '1'}) == "KeyError"

def test_invert_3():
    """Tests to see if sample list is inverted."""
    assert invert({'b': 'bcd', 'k' : 'yda', 'l': 'xad'}) == {'bcd': 'b', 'yda' : 'k', 'xad': 'l'}