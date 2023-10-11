#!/usr/bin/python3
"""Def a file-appending fun."""


def append_write(filename="", text=""):
    """Appen a str to the end of a UTF8 text f.

    Args:
        filename (str): The name of the file to append to.
        text (str): The str to append to the f.
    Returns:
        The num of char appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)i
