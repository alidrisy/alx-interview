#!/usr/bin/python3
""" Model for makingChange """
import sys


def makeChangeUtil(coins, m, total, dp):
    """determine the fewest number of coins needed to meet
    a given amount total"""
    if total == 0:
        return 0

    if dp[total] != -1:
        return dp[total]

    res = sys.maxsize

    for i in range(m):
        if coins[i] <= total:
            sub_res = makeChangeUtil(coins, m, total - coins[i], dp)

            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    dp[total] = res

    return res


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0
    n = len(coins)
    dp = [-1] * (total + 1)
    res = makeChangeUtil(coins, n, total, dp)
    if res == sys.maxsize:
        res = -1
    return res
