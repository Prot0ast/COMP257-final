# Author: Alan Barragan
# Project Title: COMP 257 Final Project
# Description: This is my implementation for Problem 5 Board Game problem which consists of 3 different algorithms:
# Brute-Force, Greedy, and Dynamic Programming

import numpy as np
from itertools import chain, combinations

# Helper Functions


def generate_random(n):
    v = [0] * n
    for i in range(n):
        v[i] = i + 1
    return v


def subset_maker(bridges):
    subsets = list(bridges)
    return chain.from_iterable(combinations(subsets, r) for r in range(len(subsets)+1))


# Algorithm Implementations


def brute(subsets):
    max_bridges = 0
    for x in subsets:
        n = len(x)
        overlapping = False
        for i in range(1, n):
            if x[i-1] > x[i]:
                overlapping = True
        if not overlapping:
            if len(x) > max_bridges:
                max_bridges = len(x)
    return max_bridges


def greedy(bridge_arr):
    sorted_version = sorted(bridge_arr)

    bridge_dict = {}
    for i, b in enumerate(bridge_arr):
        bridge_dict[b] = i
    indexes = [bridge_dict[a] for a in sorted_version]

    bridgeSet = [sorted_version[0]]
    for i in range(1, len(sorted_version)):
        if indexes[i-1] < indexes[i]:
            bridgeSet.append(sorted_version[i])
    return len(bridgeSet)


def dynamic(size, bridge_arr):
    DP = [0 for i in range(size)]
    for i in range(size):
        if i == 0:
            DP[i] = 1
        else:
            maxPrev = 0
            for j in range(i):
                if bridge_arr[j] < bridge_arr[i]:
                    if DP[j] > maxPrev:
                        maxPrev = DP[j]
            DP[i] = 1 + maxPrev
    return np.max(DP)


def main():
    # num_colors value to be changed whenever needed
    # num_colors = 5
    # array_bridges = generate_random(num_colors)
    array_bridges = [1, 5, 2, 4, 3]
    print("Bridge set to be checked: ", array_bridges)
    subsets = subset_maker(array_bridges)
    print("Brute solution result: ", brute(subsets))
    print("Greedy solution result: ", greedy(array_bridges))
    print("Dynamic solution result:", dynamic(len(array_bridges), array_bridges))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
