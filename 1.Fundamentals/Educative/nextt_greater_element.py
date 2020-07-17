# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 03:38:26 2020

@author: kalya
"""

#Brute force
# from Stack import MyStack

# def next_greater_element(lst):
#     # Write your code here
#     result =[]
#     for i in range(len(lst)):
#         mindiff = float('inf')
#         for j in range(i+1,len(lst)):
#             if lst[j]-lst[i] > 0:
#                 mindiff=lst[j]-lst[i]
#                 break
#         if mindiff == float('inf'):
#             result.append(-1)
#         else:
#             result.append(lst[i]+mindiff)
#     return result
from Stack import MyStack

def next_greater_element(lst):
    # Write your code here
    s = MyStack()
    res = [-1]*len(lst)

    for i in range(len(lst)-1, -1, -1):
        if not s.is_empty():
            while not s.is_empty() and lst[i]>=s.top():
                s.pop()
            if not s.is_empty():
                res[i] = s.top()
        s.push(lst[i])
    return res
