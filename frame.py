# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:14:14 2020
 @author: kalya
"""

# 012345
# ******
# *    
# *
# *
# *
# *  
def frame(n):
    mat = [[" "  for i in range(n)] for _ in range(n)]
    print(mat)
    for i in range(n):
        for j in range(n):
            if i == 0 or j==0 or j == n-1 or i == n-1:
                mat[i][j] = "*"
    print(mat)
    res = []
    for i in mat:
        res.append("".join(i))
    return res
    
print(frame(5))
    
