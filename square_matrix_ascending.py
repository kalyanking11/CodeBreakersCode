# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:57:38 2020

@author: kalya
"""

def matrix_ascending(mat):
    
    s = len(mat)
    if s==0 or s == 1:
        return mat
    d = {}
    for i in range(s):
        for j in range(s):
            if i+j in d:
                d[i+j].append(mat[i][j])
            else:
                d[i+j] = [mat[i][j]]
    print(d)
    for i in d:
        d[i].sort()
    print(d)
    for i in range(s):
        for j in range(s):
            mat[i][j] = d[i+j].pop()
    return mat
            
print(matrix_ascending([[1,3,9,4],[9,5,7,7],[3,6,9,7],[1,2,2,2]]))
print(matrix_ascending([[10,1],[7,5]]))