#!/usr/bin/python3
""" Model for makingChange """


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0

    count = 0

    coins.sort(reverse=True)
    for coin in coins:
        if total <= 0:
            break

        count = count + (total // coin)
        total = total % coin

    if total == 0:
        return count
    else:
        return -1
