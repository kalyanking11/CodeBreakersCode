# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:54:00 2020

@author: kalya
"""

def goodtuple(arr):
    if len(arr)<3:
        return 0
    c = 0
    if len(set(arr[0:3])) == 2:
        c += 1
    for i in range(1,len(arr)-2):
        print(set(arr[i-1:i+2]))
        if len(set(arr[i-1:i+2])) == 2:
            c += 1
    return c
print(goodtuple([1,2,1,2,1,1,1]))
        