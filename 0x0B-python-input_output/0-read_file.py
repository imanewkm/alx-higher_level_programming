#!/usr/bin/python3
"""function that reads a file and prints it"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
