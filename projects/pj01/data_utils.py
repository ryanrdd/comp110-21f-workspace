"""Utility functions."""

__author__ = "730314539"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows, each row represented as dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is in the second paramter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in column_table:
        first_n: list[str] = []
        for i in range(N):
            if i < len(column_table[key]):
                first_n.append(column_table[key][i])
        result[key] = first_n
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for s in column_names:
        result[s] = column_table[s]
    return result


def concat(column_tab_1: dict[str, list[str]], column_tab_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = column_tab_1
    for w in column_tab_2:
        if w in result:
            result[w] = column_tab_1[w] + column_tab_2[w]
        else:
            result[w] = column_tab_2[w]
    return result


def count(xs: list[str]) -> dict[str, int]:
    """This function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in xs:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


def helper_function(data: dict[str, int]) -> int:
    """This helper function will produce the number of students who did not participate in the question."""
    result = 0
    count: