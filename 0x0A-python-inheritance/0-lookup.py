#!/usr/bin/python3
"""Defines an object attribute lookup fun."""


def lookup(obj):
            """Ret a list of an object's available attributes."""
                        return (dir(obj))
