# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:15:04 2020

@author: kalyan
"""
from collections import Counter
def strreplace(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    if s1 is s2:
        return True
    if not s1 and not s2:
        return False
    c = 0
    if len(s1) != len(s2):
        if len(s1) > len(s2):
            d_s1 = Counter(s1)
            for i in s2:
                d_s1[s2] -= 1
            if sum(d_s1.values())>1:
                return False
        else:
            d_s2 = Counter(s2)
            for i in s2:
                d_s2[s1] -= 1
            if sum(d_s2.values())>1:
                return False
    
    elif len(s1) == len(s2):
        for i in s1:
            if i not in s2:
                c+=1
        if c>1:
            return False
    return True
print(strreplace('pal','pale'))
print(strreplace('pale','bale'))
print(strreplace('pale','baly'))
print(strreplace('','palep'))
        
    

