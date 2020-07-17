# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:54:27 2020

@author: kalya
"""


def find(A,target):
    low = 0
    high = len(A) - 1
    
    mid  = (low + high) // 2
    
    if A[mid] > target:
        high = mid -1
    elif A[mid] < target:
        low = mid + 1
        
    else:
        if mid - 1 < 0:
            return mid
        elif A[mid-1]!= target:
            return mid
        high = mid - 1