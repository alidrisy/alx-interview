#!/usr/bin/python3
""" Model for minOperations function """


def minOperations(n):
    """ Function that culculate the Minimum Operations to reach a number n """
    copy = 1
    step = 0
    num = 0
    if n == 0 or n == 1:
        return 0
    while True:
        if num > n:
            return 0
        if num == n:
            return step
        if num > 1 and n % num == 0:
            step += 1
            copy = num
        num += copy
        step += 1
