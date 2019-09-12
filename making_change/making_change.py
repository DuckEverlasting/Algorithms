#!/usr/bin/python


import sys

def making_change(amount, denominations, cache=None):
    if not cache:
        cache = [0 for i in range(amount + 1)]
        cache[0] = 1

    if amount < 0:
        return "error - use a positive amount"
    
    if cache[amount] != 0:
        return cache[amount]
    
    count = 0
    for i in range(0, len(denominations), -1):
        n = amount // denominations[i]
            for i in range(0, n + 1, -1):
                new_amount = amount - n * denominations[i]

        
        

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")