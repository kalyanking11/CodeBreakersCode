# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:06:02 2020

@author: kalya
"""

# [2,5,1,4]
def minimum_amount(arr):
    min_= arr[0]
    cost = arr[0]
    for i in range(1,len(arr)):
        
        if arr[i] - min_ >= 0:
            cost += (arr[i] - min_)
        min_ =  min(min_, arr[i])
    return cost
print(minimum_amount([2,5,1,4]))
        
        