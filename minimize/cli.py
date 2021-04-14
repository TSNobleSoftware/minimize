import os

import click

from minimize.util import get_py_files, file_processed_message
from minimize.consts import CLI_LINE_LENGTH


@click.command()
@click.argument("globs", nargs=-1)
def minimize(globs):
    globs = globs or ("./**/*",)
    files = get_py_files(globs)
    print("=" * CLI_LINE_LENGTH)
    for file in files:
        size_bytes = os.path.getsize(file)
        print(file_processed_message(file, size_bytes, size_bytes, CLI_LINE_LENGTH))
    print("-" * CLI_LINE_LENGTH)
    print("All done! \N{left-pointing magnifying glass}")
    print("=" * CLI_LINE_LENGTH)
