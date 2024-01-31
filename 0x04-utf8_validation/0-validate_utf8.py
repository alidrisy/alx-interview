#!/usr/bin/python3
""" Model for validUTF8 function """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    count = 0

    for i in data:
        if count == 0:
            if (i >> 5) == 0b110:
                count = 1
            elif (i >> 4) == 0b1110:
                count = 2
            elif (i >> 3) == 0b11110:
                count = 3
            elif (i >> 7) != 0:
                return False
        else:
            if (i >> 6) != 0b10:
                return False
            count -= 1

    return count == 0
