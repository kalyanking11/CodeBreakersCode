# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:36:19 2020

@author: kalya
"""


def answer(n,m,x1,y1,x2,y2):
    
    global c
    c = 0
    def grid(n,m,x1,y1,x2,y2):
        global c
        print(c)
        
        if x1 == x2 and y1 == y2:
            return c
        if x1<n  and y1<m :
            c+=1
            grid(n, m, x1+1, y1+1, x2, y2)
            
        elif x1>=n and y1>=n:
            c+=1
            grid(n,m, x1-1, y1-1, x2, y2)
            
        elif x1>=n and y1<n:
            c+=1
            grid(n,m,x1-1,y1,x2,y2)
            
        else:
            c+=1
            grid(n,m,x1,y1-1,x2,y2)
            
        
    grid(n,m,x1,y1,x2,y2)
    return c 
print(answer(5,5,2,1,1,2))          
    
        
    