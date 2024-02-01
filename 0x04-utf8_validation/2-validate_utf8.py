#!/usr/bin/python3
""" Model for validUTF8 function """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
        there is three ways to solve this problem check 1-validate_utf8.py and
        0-validate_utf8.py to see the other ways
    """

    data = [i % 256 for i in data]
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
