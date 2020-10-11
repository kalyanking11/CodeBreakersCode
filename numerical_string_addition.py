# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:26:46 2020

@author: kalya
"""

def numerical_strings(a, b):
    la = len(a)
    lb = len(b)
    if lb > la:
        return numerical_strings(b, a)
    diff = la - lb
    print(diff)
    res = list(a[:diff])
    print(res)
    list_a = list(a[diff:])
    list_b = list(b)
    for d in range(len(list_a)):
        res.append(str(int(list_a[d])+int(list_b[d])))
    # print(list_a,list_b)
    # d = diff
    # while d < len(a):
    #     # print(list_a[d],list_b[d])
    #     # print(str(int(list_a[d]+list_b[d])))
    #     res.append(str(int(list_a[d])+int(list_b[d-diff-1])))
    #     d+=1
    # print(res)
    return "".join(res)

print(numerical_strings('11','9'))
    
    
    