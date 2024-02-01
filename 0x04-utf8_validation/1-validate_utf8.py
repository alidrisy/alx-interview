#!/usr/bin/python3
""" Model for validUTF8 function """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
        there is three ways to solve this problem check 0-validate_utf8.py and
        2-validate_utf8.py to see the other ways.
    """

    for i in data:
        i %= 256
        if count == 0:
            if (i >> 5) == 6:
                count = 1
            elif (i >> 4) == 14:
                count = 2
            elif (i >> 3) == 30:
                count = 3
            elif (i >> 7) != 0:
                return False
        else:
            if (i >> 6) != 2:
                return False
            count -= 1

    return count == 0
