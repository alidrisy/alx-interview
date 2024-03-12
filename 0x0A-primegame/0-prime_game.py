#!/usr/bin/python3
""" Prime Game """


def SieveOfEratosthenes(n):
    """Return a list of  all primes smaller than or equal to n."""
    bool_prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        if bool_prime[p] == True:

            for i in range(p * p, n + 1, p):
                bool_prime[i] = False
        p += 1
    prime = []
    for p in range(1, n + 1):
        if bool_prime[p]:
            prime.append(p)
    return prime


def isWinner(x, nums):
    """Determine who the winner of the prime game."""
    ben = 0
    maria = 0
    round = "maria"
    i = 0

    while x > 0:

        prime = SieveOfEratosthenes(nums[i])
        n = len(prime) - 1

        if len(prime) == 1 and i == len(nums) - 1:
            if round == "maria":
                round = "ben"
                maria += 1
            elif round == "ben":
                round = "maria"
                ben += 1

        for y in range(n, 0, -1):
            if round == "maria":
                round = "ben"
                if y == 1:
                    maria += 1
                    print("maria")
                continue
            elif round == "ben":
                round = "maria"
                if y == 1:
                    ben += 1
                    print("ben")
                continue
        x -= 1
        i += 1

    if maria > ben:
        return "maria"
    elif ben > maria:
        return "ben"
    else:
        return None
