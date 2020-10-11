# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:09:14 2020

@author: kalya
"""

def swap(s, sizes):
    res = []
    res.append(s[:sizes[0]])
    for i in range(1, len(sizes)):
        sizes[i]+=sizes[i-1]
    for i in range(1,len(sizes)):
        res.append(s[sizes[i-1]:sizes[i]])
    #print(res)
    if len(res) % 2 == 0:
        for i in range(0,len(res)-1,2):
            #print(res[i])
            res[i], res[i+1] = res[i+1], res[i]
    else:
        
        for i in range(0,len(res)-2,2):
            #print(res[i])
            res[i], res[i+1] = res[i+1], res[i]
            
    return ''.join(c for c in res)
            
print(swap('descognail',[3,2,3,1,1]))