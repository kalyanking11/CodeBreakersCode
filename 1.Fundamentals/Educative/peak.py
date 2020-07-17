# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 02:36:13 2020

@author: kalya
"""


def find_highest_number(A):
    low = 0
    high =len(A) - 1
    
    if len(A) < 3:
        return None
    
    while low<=high:
        mid = (low+high)//2
        
        mid_left = A[mid - 1] if mid-1>0 else float("-inf")
        mid_right = A[mid + 1] if mid+1<len(A) else float("inf")
        
        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left< A[mid] and mid_right< A[mid]:
            return A[mid]
    return None