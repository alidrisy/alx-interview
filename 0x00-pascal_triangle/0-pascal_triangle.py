#!/usr/bin/python3
"""Pascal’s triangle function"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal’s triangle of n
    """
    pascal_list = []
    list1 = []
    if n < 1:
        return pascal_list
    for i in range(n):
        if i == 0 or i == 1:
            pascal_list.append(1)
            list1.append(pascal_list.copy())
            continue
        for s in range(len(pascal_list)):
            if s == len(pascal_list) - 1:
                continue
            pascal_list[s] += pascal_list[s + 1]
        pascal_list.insert(0, 1)
        list1.append(pascal_list.copy())
    return list1
