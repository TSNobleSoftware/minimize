from minimize.core import (
    strip_comments,
    strip_extra_newlines,
    strip_trailing_whitespace,
)


def test_strip_comments():
    assert strip_comments(b"#foo\nbar") == b"\nbar"
    assert strip_comments(b"bar #foo") == b"bar "


def test_strip_extra_newlines():
    assert strip_extra_newlines(b"foo\n\n\n") == b"foo\n"


def test_strip_trailing_whitespace():
    assert strip_trailing_whitespace(b"foo     \n") == b"foo\n"
    assert strip_trailing_whitespace(b"foo\t\t\t\n") == b"foo\n"
