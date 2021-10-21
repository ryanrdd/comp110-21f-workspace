"""Unit tests for dictionary functions."""

__author__ = "730314539"


from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_1():
    """Tests to see if a sample list gets inverted."""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2():
    """Tests to see if the list returns KeyError."""
    assert invert({'kris': 'jordan', 'michael': 'jackson'}) == {'jordan': 'kris', 'jackson': 'michael'}


def test_invert_3():
    """Tests to see if sample list is inverted."""
    assert invert({'b': 'bcd', 'k' : 'yda', 'l': 'xad'}) == {'bcd': 'b', 'yda' : 'k', 'xad': 'l'}


def test_favorite_colors_1():
    """Tests to see if a sample list gets inverted."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_colors_2():
    """Tests to see if the list returns KeyError."""
    assert favorite_color({"Marc": "pink", "Ezri": "pink", "Kris": "pink"}) == "pink"


def test_favorite_colors_3():
    """Tests to see if sample list is inverted."""
    assert favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "blue"}) == "yellow"


def test_count_1():
    """Tests to see if a sample list gets inverted."""
    d: list[str] = ["0", "1", "4", "5"]
    assert count(d) == {'0': 1, '1': 1, '4': 1, '5': 1}


def test_count_2():
    """Tests to see if the list returns KeyError."""
    d: list[str] = ["Ka", "Ki", "Li", "Son"]
    assert count(d) == {'Ka': 1, 'Ki': 1, 'Li': 1, 'Son': 1}


def test_count_3():
    """Tests to see if sample list is inverted."""
    d: list[str] = ["F", "A", "N", "S"]
    assert count(d) == {'F': 1, 'A': 1, 'N': 1, 'S': 1}