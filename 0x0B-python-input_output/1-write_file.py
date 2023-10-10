#!/usr/bin/python3
# 1-number_of_lines.py
# Brennan D Baraban <375@holbertonschool.com>
"""Def a text f line-counting fun."""


def number_of_lines(filename=""):
    """R the num of lines in a text f."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
