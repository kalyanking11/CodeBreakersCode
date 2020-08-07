# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:44:36 2020

@author: kalyan
"""
# target = 9      l
#                 h        
# 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8
def binary_search(arr,target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

print(binary_search([1 ,2 ,3 ,4, 5, 6, 7, 8 ,9], 9))

        