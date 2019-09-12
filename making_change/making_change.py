#!/usr/bin/python
import sys


def making_change(amount, denominations, cache=None):
    if amount == 0 or len(denominations) == 0:
        return 1
    
    count = 0
    coin = denominations[-1]
    new_denom = denominations [:-1]

    for i in reversed(range(0, (amount // coin) + 1)):
        if amount - (coin * i) == 0:
            count += 1
        elif len(new_denom) > 0:
            count += making_change(amount - coin * i, new_denom)
    
    return count

# d = [1,5,10]
# test = []
# for i in range(1, 300):
#     a = making_change(i, d) 
#     b = making_change(i - 1, d)
#     if a > b:
#         test.append([i, a, a - b])
# for i in range(0, len(test)):
#     if i != 0:
#         test[i].append(test[i][2] - test[i - 1][2])
#     print(test[i])
# for i in range(1, 100):
#     print(i, "-", making_change(i, d))


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")