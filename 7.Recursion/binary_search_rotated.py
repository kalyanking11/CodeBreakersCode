# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:58:35 2020

@author: kalyan
"""

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# target : 5               l
#                          h
# [6, 7, 8, 9, 1, 2, 3, 4, 5]
#  0  1  2  3  4  5  6  7  8 
# 
# [2, 2, 2, 3, 3, 3, 3, 4, 4, 4]


# target = 3
#                 l     m     h
# [4, 4, 4, 2, 2, 2, 3, 3, 3, 3]
#  0  1  2  3  4  5  6  7  8  9

# [2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
# target = 3

#  l           m              h
# [2, 2, 2, 3, 2, 2, 2, 2, 2, 2]
#  0  1  2  3  4  5  6  7  8  9

def binary_search_rotated (arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] ==  target:
            return mid
        elif arr[lo] > arr[mid]:
            if target>= arr[lo] or target<= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
def binary_search_rotated_duplicates (arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] ==  target:
            return mid
        while(lo!=mid and arr[lo] == arr[mid]):
            lo+=1
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target<= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
    
    
    