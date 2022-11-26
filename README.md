# COMP257 Final Project

## Problem Description:

The problem I have selected is the board game problem. Within this problem, a user is presented with a random assortment of n colored board pieces to which only two pieces from the set share a color with each other. Within the randomly sorted board, the user is allowed to create a bridge between the colors under the following conditions:

- The two pieces share the same color
- The two pieces do not overlap a pre-existing bridge when the bridge is generated

The main goal of this board game is to be able to generate as many bridges within the set as possible while abiding by these requirements. 

In terms of the inputs needed for this, this will take in the input of the n pieces that get generated into an array of bridges of size n such that we end up with the following: [1, 2, 3, ... n]. This array will be treated as the potential bridges that could be generated. In terms of output, we will get a number that is the maximum number of bridges that can be generated within a given random bridge array set.
