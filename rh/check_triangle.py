# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:25:29 2020

@author: kalya
"""
def check(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
def can_form(arr):
    res = []
    for i in range(len(arr)-2):
        if check(arr[i],arr[i+1],arr[i+2]):
            res.append(1)
        else:
            res.append(0)
    return res
print(can_form([1,2,2,4]))
            