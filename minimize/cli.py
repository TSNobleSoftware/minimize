import os

import click

from minimize.util import get_py_files, file_processed_message
from minimize.core import (
    strip_comments,
    strip_extra_newlines,
    strip_trailing_whitespace,
)
from minimize.consts import CLI_LINE_LENGTH


@click.command()
@click.argument("globs", nargs=-1)
def minimize(globs):
    globs = globs or ("./**/*",)
    files = get_py_files(globs)
    print("=" * CLI_LINE_LENGTH)
    for file in files:
        size_before_bytes = os.path.getsize(file)
        # TODO: pull out this process into a "pipeline", reading bytes at the start,
        #  passing transformed bytes between an arbitrary number of steps, and writing
        #  out the bytes at the end
        with open(file, "rb") as source:
            bytes = source.read()
        bytes = strip_comments(bytes)
        bytes = strip_extra_newlines(bytes)
        bytes = strip_trailing_whitespace(bytes)
        with open(file, "wb") as source:
            source.write(bytes)
        size_after_bytes = os.path.getsize(file)
        print(
            file_processed_message(
                file, size_before_bytes, size_after_bytes, CLI_LINE_LENGTH
            )
        )
    print("-" * CLI_LINE_LENGTH)
    print("All done! \N{left-pointing magnifying glass}")
    print("=" * CLI_LINE_LENGTH)


if __name__ == "__main__":
    minimize()
