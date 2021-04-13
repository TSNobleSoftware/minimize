import os

import click

from minimize.util import get_py_files, file_processed_message

LINE_LENGTH = 80


@click.command()
@click.argument("globs", nargs=-1)
def minimize(globs):
    globs = globs or ("./**/*",)
    files = get_py_files(globs)
    print("=" * LINE_LENGTH)
    for file in files:
        size_bytes = os.path.getsize(file)
        print(file_processed_message(file, size_bytes, size_bytes, LINE_LENGTH))
    print("-" * LINE_LENGTH)
    print("All done! \N{left-pointing magnifying glass}")
    print("=" * LINE_LENGTH)


if __name__ == "__main__":
    minimize()
