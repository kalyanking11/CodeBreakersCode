# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:15:23 2020

@author: kalya
"""


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    
    mid = (low+high)//2
    
    while low <= high:
        if data[mid] == target:
            return True
        elif data[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def binary_search_recursive(data, target, low, high):
    if low>high:
        return False
    mid = (low+high)//2
    
    if data[mid] == target:
        return True
    elif data[mid]<target:
        return binary_search_recursive(data, target, mid+1, high)
    else:
        return binary_search_recursive(data, target, low, mid-1)
    