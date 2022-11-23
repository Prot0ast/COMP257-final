# Author: Alan Barragan
# Project Title: COMP 257 Final Project
# Description: This is my implementation for Problem 5 Board Game problem which consists of 3 different algorithms:
# Brute-Force, Greedy, and Dynamic Programming

# Helper Functions


def generate_random(n):
    v = [0] * n
    for i in range(n):
        v[i] = i + 1
    return v


def subset_maker(bridges):
    subsets = [[]]
    for i in range(len(bridges) + 1):
        for j in range(i):
            subsets.append(bridges[j: i])
    return subsets


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
    bridgeSet = []
    n = len(sorted_version[1:])
    bridge_dict = {}
    for i, b in enumerate(bridge_arr):
        bridge_dict[b] = i
    indexes = [bridge_dict[a] for a in sorted_version]
    bridgeSet.append(sorted_version[0])
    for i in range(1, n):
        if bridgeSet[i - 1] <= sorted_version[i] and indexes[i-1] <= indexes[i]:
            bridgeSet.append(sorted_version[i])
    return len(bridgeSet)


def main():
    # num_colors value to be changed whenever needed
    num_colors = 5
    # array_bridges = generate_random(num_colors)
    print("Bridge set to be checked: ", [5, 4, 1, 2, 3])
    subsets = subset_maker([5, 4, 1, 2, 3])
    # print("Subsets for the bridge set: ", subsets)
    print("Brute solution result: ", brute(subsets))
    print("Greedy solution result: ", greedy([5, 4, 1, 2, 3]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
