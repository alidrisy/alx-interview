#!/usr/bin/python3
""" Function canUnlockAll to determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. """
    if len(boxes[0]) == 0:
        return False
    for i in range(len(boxes)):
        for k in boxes[i]:
            if k != i and True not in boxes[k] and type(k) is int:
                boxes[k].append(True)
    for i in range(1, len(boxes)):
        if True not in boxes[i]:
            return False
    return True
