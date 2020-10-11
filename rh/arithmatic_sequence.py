# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:36:55 2020

@author: kalya
"""

def arithmatic(a, b):
    m = float('inf')
    for i in range(1,len(a)):
        m = min(m, a[i]-a[i-1])
    #print(m)
    res = set()
    k = f = a[0]
    res.add(f)
    
    while k>=0:
        k = k-m
        if k in b:
            res.add(k)
    c = 1
    while (f+m in a) or (f+m in b):
        if f+m in a:
            c+=1
        res.add(f+m)
        f += m
    if c == len(a):
        return res
    return -1
        
    
            
    
    
    
    
    
    
    

# a  = [8, 12,14, 16]
# b  = [0, 4, 8, 20]
a  = [5, 7, 13, 14]
b  = [9, 11, 15]
print(arithmatic(a,b))