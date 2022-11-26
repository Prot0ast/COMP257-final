# COMP257 Final Project

## Problem Description:

The problem I have selected is the board game problem. Within this problem, a user is presented with a random assortment of n colored board pieces to which only two pieces from the set share a color with each other. Within the randomly sorted board, the user is allowed to create a bridge between the colors under the following conditions:

- The two pieces share the same color
- The two pieces do not overlap a pre-existing bridge when the bridge is generated

The main goal of this board game is to be able to generate as many bridges within the set as possible while abiding by these requirements. 

In terms of the inputs needed for this, this will take in the input of the n pieces that get generated into an array of bridges of size n such that we end up with the following: [1, 2, 3, ... n]. This array will be treated as the potential bridges that could be generated. In terms of output, we will get a number that is the maximum number of bridges that can be generated within a given random bridge array set.

## Pseudocode for Brute Force Algorithm:
This algorithm takes in the n-sized array of bridges and obtains each possible subset from it and returns the subset that has the largest possible amount of bridges that can be generated. Whenever a subset can surpass the current maximum number of bridges it gets updated and replaced, otherwise it stays the same.
```python

def subset_maker(n_sized_bridges):
  subsets = [[]]
  for i in range(len(n_sized_bridges) + 1);
    for j in range(i):
      subsets.append(n_sized_bridges[j:i])
 return subsets

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
  ```

