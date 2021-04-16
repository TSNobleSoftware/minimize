import string

from minimize.util import unique, unique_symbol_generator


def test_unique():
    assert unique([1, 2, 3]) == [1, 2, 3]
    assert unique([1, 1, 2, 2, 3, 3]) == [1, 2, 3]


def test_unique_symbol_generates_alphabet():
    symbols = unique_symbol_generator()
    letters = [next(symbols) for _ in range(52)]
    assert letters == list(string.ascii_lowercase + string.ascii_uppercase)


def test_unique_symbol_prefixes_with_underscore_once_all_letters_are_used():
    symbols = unique_symbol_generator()
    _ = [next(symbols) for _ in range(52)]
    prefixed_letters = [next(symbols) for _ in range(52)]
    assert all([symbol.startswith("_") for symbol in prefixed_letters])
