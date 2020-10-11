# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:21:20 2020

@author: kalya
"""

def arr(m,n,queries):
    invalid_row, invalid_col = [],[]
    mr, mc = 1, 1
    res = []
    for q in queries:
        if q == [0]:
            res.append( mr*mc)
        elif q[0] == 1:
            invalid_row.append(q[1])
            # print("row")
            # print(invalid_row)
            if mr in invalid_row:
                while mr in invalid_row :
                    mr+=1
        else:
            invalid_col.append(q[1])
            # print("col")
            # print(invalid_col)
            if mc in invalid_col:
                while mc in invalid_col:
                    mc+=1
    return res

print(arr(3,4,[[0],[1,1],[0],[1,2],[0],[1,3],[0]]))

                