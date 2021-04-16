import re
import tokenize
from io import BytesIO


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


def strip_operator_whitespace(bytes):
    one_char_ops = r"\+|-|\*|%|/|,|=|\(|\)|\[|\]|\{|\}|:"
    two_char_ops = r"\+=|-=|\*=|%=|/=|=="
    pre_space = rf"([ \t]*(?={one_char_ops}))|([ \t]*(?={two_char_ops}))"
    post_space = rf"((?<={one_char_ops})[ \t]*)|((?<={two_char_ops})[ \t]*)"
    pre_or_post_space = rf"({pre_space})|({post_space})".encode("utf-8")
    return re.sub(pre_or_post_space, b"", bytes)


def replace_spaces_with_tabs(bytes):
    return re.sub(b" {4}", b"\t", bytes)
