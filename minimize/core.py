import re


def strip_comments(bytes):
    lines = bytes.split(b"\n")
    comment = rb"#.*"
    return b"\n".join([re.sub(comment, b"", line) for line in lines])


def strip_extra_newlines(bytes):
    two_plus_newlines = rb"\n\n+"
    return re.sub(two_plus_newlines, b"\n", bytes)


def strip_trailing_whitespace(bytes):
    trailing_whitespace = rb"\s+\n"
    return re.sub(trailing_whitespace, b"\n", bytes)
