# Author: Alan Barragan
# Project Title: COMP 257 Final Project
# Test cases

import final as foon
from timeit import default_timer as timer


def main():
    # Test case #1
    print("Test case #1 - Single Entry Array")
    start = timer()
    print("Brute solution: ", foon.brute(foon.subset_maker([1])))
    endtime = timer()
    total = endtime - start
    print("Brute time: ", total)

    start = timer()
    print("Greedy solution: ", foon.greedy([1]))
    endtime = timer()
    total = endtime - start
    print("Greedy time: ", total)

    start = timer()
    print("Dynamic solution: ", foon.dynamic(len([1]), [1]))
    endtime = timer()
    total = endtime - start
    print("Dynamic time: ", total)
    print()

    # Test case #2
    print("Test case #2 - Three-Entry Array in Order")
    start = timer()
    print("Brute solution: ", foon.brute(foon.subset_maker([1, 2, 3])))
    endtime = timer()
    total = endtime - start
    print("Brute time: ", total)

    start = timer()
    print("Greedy solution: ", foon.greedy([1, 2, 3]))
    endtime = timer()
    total = endtime - start
    print("Greedy time: ", total)

    start = timer()
    print("Dynamic solution: ", foon.dynamic(len([1, 2, 3]), [1, 2, 3]))
    endtime = timer()
    total = endtime - start
    print("Dynamic time: ", total)
    print()

    # Test case #3
    print("Test case #3 - Three-Entry Array not in Order")
    start = timer()
    print("Brute solution: ", foon.brute(foon.subset_maker([3, 2, 1])))
    endtime = timer()
    total = endtime - start
    print("Brute time: ", total)

    start = timer()
    print("Greedy solution: ", foon.greedy([3, 2, 1]))
    endtime = timer()
    total = endtime - start
    print("Greedy time: ", total)

    start = timer()
    print("Dynamic solution: ", foon.dynamic(len([3, 2, 1]), [3, 2, 1]))
    endtime = timer()
    total = endtime - start
    print("Dynamic time: ", total)
    print()

    # Test case #4
    print("Test case #4 - Five-Entry Array with 3 values in order in sequence")
    start = timer()
    print("Brute solution: ", foon.brute(foon.subset_maker([5, 4, 1, 2, 3])))
    endtime = timer()
    total = endtime - start
    print("Brute time: ", total)

    start = timer()
    print("Greedy solution: ", foon.greedy([5, 4, 1, 2, 3]))
    endtime = timer()
    total = endtime - start
    print("Greedy time: ", total)

    start = timer()
    print("Dynamic solution: ", foon.dynamic(len([5, 4, 1, 2, 3]), [5, 4, 1, 2, 3]))
    endtime = timer()
    total = endtime - start
    print("Dynamic time: ", total)
    print()

    # Test case #5
    print("Test case #5 - Five-Entry Array with 3 values in order not in sequence")
    start = timer()
    print("Brute solution: ", foon.brute(foon.subset_maker([1, 5, 2, 4, 3])))
    endtime = timer()
    total = endtime - start
    print("Brute time: ", total)

    start = timer()
    print("Greedy solution: ", foon.greedy([1, 5, 2, 4, 3]))
    endtime = timer()
    total = endtime - start
    print("Greedy time: ", total)

    start = timer()
    print("Dynamic solution: ", foon.dynamic(len([1, 5, 2, 4, 3]), [1, 5, 2, 4, 3]))
    endtime = timer()
    total = endtime - start
    print("Dynamic time: ", total)
    print()


if __name__ == '__main__':
    main()