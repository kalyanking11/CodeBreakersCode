# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:30:56 2020

@author: kalyan
"""
# 10 9 8 7 6 5 4 3 2 1
def InsertionSort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr
