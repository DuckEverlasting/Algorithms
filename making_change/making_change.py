#!/usr/bin/python
import sys

def making_change(amount, denominations, cache=None):
    if not cache:
        cache = {}

    if amount == 0 or len(denominations) == 0:
        return 1
    
    if cache[f"{amount}_{denominations}"]:
        print("DING")
        return cache[f"{amount}_{denominations}"]

    count = 0
    coin = denominations[0]
    new_denom = denominations [1:]

    for i in range(0, (amount // coin) + 1):
        if amount - (coin * i) == 0:
            count += 1
        elif len(new_denom) > 0:
            count += making_change(amount - coin * i, new_denom, cache)
            
    cache[f"{amount}_{denominations}"] = count
    return count

print("[1, 5, 10, 25, 50]", making_change(61, [1, 5, 10, 25, 50]))


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")