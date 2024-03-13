#!/usr/bin/python3
""" Prime Game """


def get_prime(n):
    """Return a list of  all primes smaller than or equal to n."""
    bool_prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        if bool_prime[p]:

            for i in range(p * p, n + 1, p):
                bool_prime[i] = False
        p += 1
    prime = 0
    for p in range(2, n + 1):
        if bool_prime[p]:
            prime += 1
    return prime


def isWinner(x, nums):
    """Solves Prime Game"""
    if not nums or x < 1:
        return None
    ben = 0
    maria = 0
    for num in nums:
        prime = get_prime(num)
        if prime % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
