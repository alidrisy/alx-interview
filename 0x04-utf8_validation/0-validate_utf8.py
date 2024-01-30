#!/usr/bin/python3
""" Model for validUTF8 function """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding. """
    if all(i < 256 for i in data):
        return True
    return False
