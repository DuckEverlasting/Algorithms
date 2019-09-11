#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# WHO YOU CALLIN' NAIVE?

# Cookie Monster can eat range(0, 4) cookies
# It looks like with "0", they're just referring to the edge case of n = 0
# def eating_cookies(n, cache=None):
#     if n == 0:
#         print("FINAL:", 1)
#         return 1
    
#     if not cache or isinstance(cache, list):
#         cache = {}
#         cache["count"] = 0
#         cache["max"] = n
#         n = []
#         cur_sum = 0
#     else:
#         cur_sum = sum(n)

#     if cur_sum < cache["max"]:
#         for i in (j for j in range(1, cache["max"] + 1 - cur_sum) if j <= 3):
#             try:
#                 return cache[f"{n + [i]}"]
#             except:
#                 cache[f"{n + [i]}"] = True
#                 eating_cookies(n + [i], cache)
#     else:
#         cache["count"] += 1
    
#     return cache["count"]

def eating_cookies(n, cache=None):
    if not cache:
        cache = [0 for i in range(n)]

    if n == 0:
        return 1

    if n == 1:
        if cache[1] == 0:
            cache[1] = 1
        return 1

    if n == 2:
        if cache[2] == 0:
            cache[2] = 2
        return 2

    if n == 3:
        if cache[3] == 0:
            cache[3] = 4
        return 4

    return len(cache)


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

