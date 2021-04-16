import glob
import itertools
import string
import math


def unique(_list):
    return list(set(_list))


def get_py_files(globs):
    py_files = [file for g in globs for file in glob.glob(g) if file.endswith(".py")]
    return unique(py_files)


def file_processed_message(filename, original_size, reduced_size, line_length):
    percent = get_percent_reduced(original_size, reduced_size)
    filename_string = f"Minimized {filename}"
    info_string = f"{original_size} bytes -> {reduced_size} bytes ({percent:.2f}%)"
    padding = line_length - len(filename_string)
    return f"{filename_string}{info_string:>{padding}}"


def get_percent_reduced(original, reduced):
    try:
        percent_reduced = 100 - (reduced / original) * 100
    except ZeroDivisionError:
        percent_reduced = 0
    return percent_reduced


def unique_symbol_generator():
    letters = string.ascii_lowercase + string.ascii_uppercase
    for index in itertools.count():
        yield f"{'_' * math.floor(index / 52)}{letters[index % 52]}"
