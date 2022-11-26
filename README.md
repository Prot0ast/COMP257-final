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
  
## Pseudocode for Greedy Algorithm:
This algorithm takes in the n_sized array of bridges, sorts them into ascending order, then apends each instance of the sorted array onto a separate list if and only if the value of the array does not overlap with a previous entry in the list. The reason why the list gets sorted is so that we can start from the smallest value in the set and work our way up to the largest value in the set, just like how greedy algorithms tend to operate. This algorithm will return the length of the numbers appended to the separate list as that would be the total maximum number of bridges that can be generated by the given n-set. 
```python

def greedy(n_sized_array):
  sorted_arr = sorted(n_sized_array):
  
  bridge_dict = {}
  for i,b in enumerate(n_sized_array):
    bridge_dict[b] = i
  indexes = [bridge_dict[a] for a in sorted_arr]
  
  bridgeSet = []
  for in range(len(sorted_arr)):
    if indexes[i-1] < indexes[i]:
      bridgeSet.append(sorted_arr[i])
  return len(bridgeSet)
```

## Pseudocode for Dynamic Programming Algorithm:
This algorithm takes in both the size of the n_sized array of bridges alongside the n_sized array of bridges to which it generates a storage space that is the same size as the (you guessed it) n_sized array of bridges and updates the values to it in accordance to the problem. Since this method builds up to the solution, it updates the value of the storage space so long as the value within the n_sized array of bridges is less than the previous entry as that would indicate that it is not overlapping. Since this method is very similar to that of the longest increasing subsequence problem, we will also be returning the maximum number from the subsequence as that would be the maximum number of bridges that can be generated.
```python
def dynamic(size, n_sized_array):
storage = [# for i in range(size)] # The # does not matter as this gets updated for each n element in 
                                   # n_sized_array
for i in range(size):
  if i == 0:
    storage[i] = 1
  else:
    maxPrev = 0
    for j in range(i - 1):
      if n_sized_array[j] < n_sized_array[i]:
        if storage[j] > maxPrev:
          maxPrev = storage[j]
    storage[i] = 1 + maxPrev
 return maximum of storage[size - 1]
```

## Time Complexities
| Type of Algorithm | Big-O | Explanation |
| :---------------- | :---- | :---------- |
| Brute-Force       | O(n^2)| Since this algorithm utilizes two for-loops of size n (based on the bridges), this results in a O(n * n) which when simplified is O(n^2). Though my implementation of this algorithm uses a helper function to make subsets, that only takes O(n) which ends up performing faster than the brute force itself which is O(n^2) and as thus cannot be considered as the Big-O runtime for it. |
| Greedy            | O(n^2)| This takes O(n^2) as well for my given implementation as it goes through one for-loop to generate the subsets of the n_sized_array of bridges and goes through another for-loop to append each value of the sorted version array that abides by the given rules of the problem. |
| Dynamic Programming| O(n^2)| This algorithm takes O(n^2) as well since it utilizes a nested for-loop that iterates through the size of the n_sized array and checks for each entry that is behind the current index inside of the for-loop to check if the value itself is overlapping or not so that it can append it to the list. |

## Outputs

### Test Case 1
![image](https://user-images.githubusercontent.com/56521346/204110378-8f1e7912-fbb9-453f-9197-63543149b92d.png)

### Test Case 2
![image](https://user-images.githubusercontent.com/56521346/204110803-11fd781b-e364-4490-9efc-58f28cfcfe90.png)

### Test Case 3
![image](https://user-images.githubusercontent.com/56521346/204110790-ffae6087-9989-444d-9dfa-9e0f01635f98.png)

### Test Case 4
![image](https://user-images.githubusercontent.com/56521346/204110807-699cc549-7650-44f6-9977-cbd2e485c93e.png)

### Test Case 5
![image](https://user-images.githubusercontent.com/56521346/204110810-d04754e8-f6ba-452b-916c-3ba3521c34e0.png)

## Missing Test Cases & Greedy Algorithm Different Solution Explanations

### Testing for an empty array
Due to the given nature of how I have implemented the dynamic algorithm to add the first value in the sorted array onto the DP array to allow for comparisons to the previous value, I cannot test for an empty array as this will result in an exception. To make up for this, this is the reasoning as to why I opted for a single-entry array test as this is the closest to zero.

### Algorithms resulting in some different results
With how I have implemented the algorithms, there are certain instances in which there are different solutions for each of the algorithms such as moments in which one algorithm will say that the maximum total bridges is less than or more than what other algorithms propose to be the optimal solution. This behavior is to be expected given the nature of how each of these are implemented.

## Plot of Test Case Size & Time Taken
![image](https://user-images.githubusercontent.com/56521346/204111475-447395dc-e3f6-44ba-bcd5-8e5fe196fec6.png)

## Algorithm Recommendation
After analyzing each of the algorithms both in terms of correctness and time efficiency, I would opt for going with the Greedy Algorithm in such case. Though it is slower than the Brute force solution for each instance, it is the most consistent in finding the correct number of total maximum bridges as it passes each of my proposed test cases. Though brute was correct for 4/5 of the test cases, Greedy is more consistent with it passing all of them. I would not recommend running Dynamic for this problem as not only was it the most inconsistent but it also took the most time compared to the others; to which I find this very interesting considering that the Brute force method is the fastest of the three while also being the least optimal. Greedy is definitely the way to go with this board game bridge building problem.
