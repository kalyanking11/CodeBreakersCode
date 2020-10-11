# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:57:33 2020

@author: kalya
"""

def str_count(t, s):
    l = len(t)
    c = 0
    for i in range(l-4):
        if t[i] == s[0] and t[i+2] == s[1] and t[i+4] == s[2]:
            c+=1
    return c
print(str_count('azcabcab','acb'))
print(str_count('','xyz'))