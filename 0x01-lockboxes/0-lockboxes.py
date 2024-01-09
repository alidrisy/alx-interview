#!/usr/bin/python3
""" Function canUnlockAll to determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. """
    if len(boxes[0]) == 0:
        return False
    boxes[0].append("open")
    x = 0
    while x < 2:
        for i in range(len(boxes)):
            if "open" in boxes[i]:
                for k in boxes[i]:
                    if type(k) is int and k < len(boxes) and k != i and\
                            "open" not in boxes[k]:
                        boxes[k].append("open")
            x += 1
    for i in range(len(boxes)):
        if "open" not in boxes[i]:
            return False
    return True
