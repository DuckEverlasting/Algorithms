#!/usr/bin/python

import sys


def rock_paper_scissors(n, cache=None):
    # set up cache on initial call
    if not cache:
        cache = [[[]]] + [0 for i in range(n)]

    # return from cache when possible
    if cache[n] != 0:
        return cache[n]

    # declare possible moves
    moves = [["rock"], ["paper"], ["scissors"]]

    # set blank array for result
    result = [0 for i in range(3 ** n)]

    # recursive loop to set up previous result
    prev_result = rock_paper_scissors(n - 1)
    
    # add "rock", "paper", and "scissors" to each item from the last result
    for i in range(3 ** n):
        result[i] = prev_result[i // 3] + moves[i % 3]

    # set cache and return
    cache[n] = result
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

