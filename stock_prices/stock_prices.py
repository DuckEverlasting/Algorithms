#!/usr/bin/python

import argparse

# prices = list of stock prices
# find greatest difference between l and r, when l comes before r
def find_max_profit(prices):
    if len(prices) < 2:
        return "error: array too small"

    largest = prices[1] - prices[0]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > largest:
                largest = prices[j] - prices[i]

    return largest

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

