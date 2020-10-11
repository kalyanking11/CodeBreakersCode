# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 23:37:13 2020

@author: kalya
"""

def diagnol(arr,n):
    mat = [[0]*n for _ in range(n)]
    k = 0
    m = n
    i, j= n-1, n-1
    
    h = True
    
    while i<=n and j<=m and k<len(arr):
        print(i,j)
        if not h:
            while i>=0:
                if mat[i][j] == 0:
                    mat[i][j] = arr[k]
                    k+=1
                i-=1
            n -= 1
            i = n
            
        else:
            while j>=0:
                if mat[i][j] == 0:
                    mat[i][j] = arr[k]
                    k += 1
                j -= 1
            m -= 1
            j = m
        # i = i-1
        # j = j-1
        h = not h
        
        print(i,j, m,n)
           
    
    
    return mat

print (diagnol([-2, -2, 1, 1, 4, 4, 3, 3 ,3],3))
        