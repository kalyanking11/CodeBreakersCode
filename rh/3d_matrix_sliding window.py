# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:58:27 2020

@author: kalya
"""

def slid(mat):
    def check(d):
        for i in d:
            if d[i]!=1:
                return False
        return True
    m = 3
    n = len(mat[0])
    res = []
    d = {}
    for i in range(1,10):
        d[i] = 0
    for i in range(m):
        for j in range(m):
            d[mat[i][j]] = 1
    print(d)
    for j in range(0,n-2):
        res.append(check(d))
        print(res)
        for i in range(m):
            d[mat[i][j]] -= 1
        if j+1<n-2:
            for i in range(m):
                print(mat[i][j+3])
                d[mat[i][j+3]] += 1
                print(d)
    return res
    


mat = [[1, 2, 3, 2, 5, 7],
       [4, 5, 6, 1, 7, 6],
       [7, 8, 9, 4, 8, 3]]

print(slid(mat))