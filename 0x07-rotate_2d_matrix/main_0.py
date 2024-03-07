#!/usr/bin/python3
""" Model for makingChange """


def makeChange(coins, total):
    """function to know the lowest number of coins"""

    if total <= 0:
        return 0

    count = 0

    coins.sort(reverse=True)
    print(coins)
    for coin in coins:
        if total <= 0:
            break

        count = count + (total // coin)
        total = total % coin

    if total == 0:
        return count
    else:
        return -1


print(makeChange([9, 6, 7, 1], 13))
print(makeChange([9, 6, 5, 1], 7))
print(makeChange([1, 2, 25], 37))


print(makeChange([1256, 54, 48, 16, 102], 1453))
