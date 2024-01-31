#!/usr/bin/python3
""" Model for validUTF8 function """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
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
    # count = 0

    # for i in data:
    #     if count == 0:
    #         if (i >> 5) == 0b110:
    #             count = 1
    #         elif (i >> 4) == 0b1110:
    #             count = 2
    #         elif (i >> 3) == 0b11110:
    #             count = 3
    #         elif (i >> 7) != 0:
    #             return False
    #     else:
    #         if (i >> 6) != 0b10:
    #             return False
    #         count -= 1

    # return count == 0
