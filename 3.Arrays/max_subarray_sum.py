# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:10:18 2020

@author: kalyan
"""

# [1, -2, 3, -5, 6, 8, -10]
# 
#
# works only for +ve numbers
# def subarray_sum(arr):
#     #kadane's algorithm
#     max_so_far = 0
#     max_ending_here = 0
#     for num in range(len(arr)):
#         max_ending_here = max_ending_here + arr[num]
#         if max_ending_here < 0:
#             max_ending_here = 0
#         elif max_ending_here > max_so_far:
#             max_so_far =  max_ending_here
#     return max_so_far
# print(subarray_sum([1, -2, 3, -5, 6, 8, -10]))
            
# for all numbers
def subarray_sum(arr):
    #kadane's algorithm
    curr_max = arr[0]
    max_so_far = arr[0]
    for num in range(1,len(arr)):
        curr_max = max(arr[num], curr_max + arr[num])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
print(subarray_sum([1, -2, 3, -5, 6, 8, -10]))










