"""Practice with dictionaries."""

__author__ = "730314539"

def invert(a: dict[str, str]) -> dict[str, str]:
    """Code that inverts the keys and values of the two lists"""
    result: dict[str, str] = {}
    for key in a:
        k: str = key
        v: str = a.pop(k)
        result[k] = v
    # for value in a:
    #     b: str = value
    #     c: str = a.pop(b)
    #     result[b] = c
    return result