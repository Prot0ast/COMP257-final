# Author: Alan Barragan
# Project Title: COMP 257 Final Project
# Test cases

import final as foon


def main():
    print("Test case #1 - Single Entry Array")
    print("Brute solution: ", foon.brute(foon.subset_maker([1])))
    print("Greedy solution: ", foon.greedy([1]))
    print("Dynamic solution: ", foon.dynamic(len([1]), [1]))


if __name__ == '__main__':
    main()