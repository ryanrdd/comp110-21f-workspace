"""Practice with dictionaries."""

__author__ = "730314539"

def invert(a: dict[str, str],b: dict[str, str]) -> dict[str, str]:
    """Code that inverts the keys and values of the two lists"""
    result: dict[str, str] = {}
    if a and b == dict[str, str]:
        for key in a:
            result[key] = b[key]
        for key in b:
            result[key] = a[key]
        return result
    else:
        raise KeyError("KeyError")