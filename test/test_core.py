import pytest

from minimize.core import (
    strip_comments,
    strip_extra_newlines,
    strip_trailing_whitespace,
    strip_operator_whitespace,
    replace_spaces_with_tabs,
)


def test_strip_comments():
    assert strip_comments(b"#foo\nbar") == b"\nbar"
    assert strip_comments(b"bar #foo") == b"bar "


def test_strip_extra_newlines():
    assert strip_extra_newlines(b"foo\n\n\n") == b"foo\n"


def test_strip_trailing_whitespace():
    assert strip_trailing_whitespace(b"foo     \n") == b"foo\n"
    assert strip_trailing_whitespace(b"foo\t\t\t\n") == b"foo\n"


@pytest.mark.parametrize(
    "op",
    [
        "+",
        "-",
        "*",
        "/",
        "%",
        ",",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "=",
        ":",
        ">",
        "<",
        "&",
        "|",
        "~",
        "+=",
        "-=",
        "*=",
        "/=",
        "%=",
        "==",
        "**",
        "//",
        "!=",
        "<>",
        ">=",
        "<=",
        ">>",
        "<<"
    ],
)
def test_strip_operator_whitespace(op):
    assert strip_operator_whitespace(f" {op} ".encode()) == op.encode()
    assert strip_operator_whitespace(f"\t{op}\t".encode()) == op.encode()
    assert strip_operator_whitespace(f"{op}\n".encode()) == f"{op}\n".encode()


def test_replace_spaces_with_tabs():
    assert replace_spaces_with_tabs(b"    ") == b"\t"
