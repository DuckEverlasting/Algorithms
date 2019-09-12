#!/usr/bin/python

import sys

# plays = (
#     ["rock", "rock"],
#     ["paper", "paper"],
#     ["scissors", "scissors"],
#     ["rock", "paper"],
#     ["paper", "scissors"],
#     ["scissors", "rock"],
#     ["rock", "scissors"],
#     ["paper", "rock"],
#     ["scissors", "paper"],
# )

def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    plays = [["rock"], ["paper"], ["scissors"]]
    results = [[] for i in range(3**n)]

    for i in range(3**n):
        for j in range(n):
            print("REMAINDER", j % 3)
            print("PLAYS REMAINDER:", plays[j % 3])
            results[i] += plays[j % 3]
            
    return results



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

