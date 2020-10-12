# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:54:38 2020

@author: kalya
"""

# def specialcodeword(n,m):
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     d = {}
#     res = ""
#     for i in range(len(alpha)):
#         d[i] = alpha[i]
    
def specialcode(n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {}
    res = ""
    for i in range(len(alpha)):
        d[i] = alpha[i]
    #print(d)
    c = 0
    for i in range(2,len(n)+1,2):
        temp = int(n[c:i])
        if temp>=26:
            temp = temp%26
        res+=d[temp]
        c+=2
    return res
            
        
        
print(specialcode('9046450429'))
print(specialcode('9952635697'))
print(specialcode('99094562465305462997'))



        
    