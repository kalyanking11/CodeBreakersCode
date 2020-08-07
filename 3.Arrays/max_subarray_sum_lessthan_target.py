# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:46:52 2020

@author: kalyan
"""
# sum of subarray less than a target k
# using sliding window technique

# [1 2 3 4 5 6]  k = 3
# -> 4
# [1]
# [1, 2] [2]
# [3]
def sumSubarray(arr, target):
    start = -1
    out = 0
    totalsum = 0
    for num in range(len(arr)):
        totalsum += arr[num]
        while totalsum > target:
            start += 1
            totalsum -= arr[start]
        out += num - start 
    return out
print(sumSubarray([1, 2, 3, 4, 5, 6], 3))