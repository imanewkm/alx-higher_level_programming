#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
