#!/usr/bin/python3
""" Model for validUTF8 function """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
        there is three ways to solve this problem check 1-validate_utf8.py and
        2-validate_utf8.py to see the other ways .. but this way is the most
        save and effective way.
    """

    masks = [128, 64, 32, 16, 8]

    def get_type(num: int) -> int:
        for i in range(5):
            if num & masks[i] == 0:
                return i
        return -1

    len_data = len(data)
    i = 0

    while i < len_data:
        curr = data[i]
        type = get_type(curr)
        if type == 0:
            i += 1
        elif type > 1 and i + type <= len_data:
            while type > 1:
                i += 1
                if get_type(data[i]) != 1:
                    return False
                type -= 1
            i += 1
        else:
            return False
    return True
