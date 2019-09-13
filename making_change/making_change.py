#!/usr/bin/python
import sys

# This assumes denominations are sorted, with the smallest denomination coming first.
# It works without sorting, but is more efficient this way. (Still could probably be much more efficient though.)
def making_change(amount, denominations):
    if amount == 0 or len(denominations) == 0:
        return 1

    count = 0
    coin = denominations[-1]
    new_denom = denominations [:-1]

    if len(new_denom) == 0:
        if amount % coin == 0:
            count += 1

    else:
        for i in range(0, (amount // coin) + 1):
            if amount - (coin * i) == 0:
                count += 1
            elif len(new_denom) > 0:
                count += making_change(amount - coin * i, new_denom)

    return count


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")