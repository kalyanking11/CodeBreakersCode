# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:30:42 2020

@author: kalyan
"""

def sortbymissingnum(mat, n):
    
    const_sum = (16*17)//2
    missing = []
    for j in range(0,4*n,4):
        
        temp_sum = 0
        x, index = -1, -1
        for i in range(4):
            print(i,j)
            if mat[i][j] == '?':
                x = i
                index = j
                temp_sum += mat[i][j+1] + mat[i][j+2] + mat[i][j+3]
                continue
            if mat[i][j+1] == '?':
                x = i
                index = j+1
                temp_sum += mat[i][j] + mat[i][j+2] + mat[i][j+3]
                continue
            
            if mat[i][j+2] == '?':
                x = i
                index = j+2
                temp_sum += mat[i][j] + mat[i][j+1] + mat[i][j+3]
                continue
            if mat[i][j+3] == '?':
                x = i
                index = j+3
                temp_sum += mat[i][j] + mat[i][j+1] + mat[i][j+2]
                continue
            temp_sum+= mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i][j+3]
        print(temp_sum)
        m = const_sum - temp_sum
        mat[x][index] = m
        print(temp_sum, m)
        missing.append((m,index//4))
        print(missing)
    missing  = sorted(missing, key = lambda x: x[0])
    print(missing,mat)
    
    ans = [[0]*len(mat[0]) for i in range(len(mat))]
    
    
    c = 0
    for i in range(len(missing)):
        val = missing[i][1]
        for j in range(4*val,4*(val+1)):
            for k in range(4):
                ans[k][c] = mat[k][j]
            c+=1
            
    return ans
    
mat = [[14,3,10,4,16,10,'?',2,'?',9,15,11],
       [16,7,8,2,1,4,8,3,3,16,7,13],
       ['?',9,6,5,14,12,7,6,2,10,4,14],
       [15,1,13,12,9,15,5,13,1,8,12,6]]
print(sortbymissingnum(mat,3))

            
            
            