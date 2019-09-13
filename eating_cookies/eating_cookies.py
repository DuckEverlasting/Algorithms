#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# WHO YOU CALLIN' NAIVE?

# Cookie Monster can eat range(0, 4) cookies
# It looks like with "0", they're just referring to the edge case of n = 0

# 1, 1, 2, 4, 7, 13, 24, 44, 81, 149
# seen that before


def eating_cookies(n, cache=None):
    if not cache:
        cache = [0 for i in range(n + 1)]

    if cache[n] != 0:
        return cache[n]

    elif n < 2:
        return 1

    elif n == 2:
        return 2

    else:
        cache[n] = (
            eating_cookies(n - 1, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 3, cache)
        )
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")

