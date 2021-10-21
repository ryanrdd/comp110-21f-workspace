"""Practice with dictionaries."""

__author__ = "730314539"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Code that inverts the keys and values of the two lists"""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError('duplicate keys in output dict')
        result[a[key]] = key
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Function that returns the most common color in a list"""
    c: dict[str, int] = {}
    c_max: int = 0
    color: str = ""
    for key in b:
        if b[key] in c:
            c[b[key]] += 1
        else:
            c[b[key]] = 1
    for key in c:
        if c[key] > c_max:
            c_max = c[key]
            color = key
    return color


def count(d: list[str]) -> dict[str, int]:
    """From a list, the function produces a count of all items in the list"""
    e: dict[str, int] = {}
    for key in d:
        if key in e:
            e[key] += 1
        else:
            e[key] = 1
    return e