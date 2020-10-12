# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def pattern(num):
    even = True
    for i in range(num):
        for k in range(i):
            print(' ',end= '')
        for j in range(i,(2*num)-i):
            if even:
                if j%2 == 0:
                    print('*',end = ' ')
            else:
                if j%2!=0:
                    print('*', end = ' ')
        even = not even
        print()
pattern(5)