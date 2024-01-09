#!/usr/bin/python3
""" Function canUnlockAll to determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. """
    if len(boxes[0]) == 0:
        return False
    boxes[0].append(True)
    for i in range(len(boxes)):
        if True in boxes[i]:
            for k in boxes[i]:
                if k < len(boxes) and k != i and True not in boxes[k] and\
                        type(k) is int:
                    boxes[k].append(True)
    for i in range(len(boxes)):
        if True not in boxes[i]:
            return False
    return True
