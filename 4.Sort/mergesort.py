# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 06:02:40 2020

@author: kalyan
"""

def mergesort(arr, low, high):
    if low >= high:
        return
    #while low<high:
    mid = ((low+high) // 2) + 1
    mergesort(arr, low, mid-1)
    mergesort(arr, mid, high)
    merge(arr,low,mid,high)
    
def merge(arr, start1, start2, end):
    
    copy = arr[:]
    cur = start1
    p1 = start1
    p2 = start2
    while cur <= end :
        if p1 < start2 and p2 <= end:
            if copy[p1] < copy[p2]:
                arr[cur] = copy[p1]
            
                p1 += 1
               
            else:
                arr[cur] = copy[p2]
                p2 += 1
                
        elif p1 < start2:
            arr[cur] = copy[p1]
            p1 += 1
           
        else:
            arr[cur] = copy[p2]
            p2 += 1
        cur+=1
    
        

arr = [1,2,3,5,4,6]
low = 0
high = len(arr) - 1

mergesort(arr, low, high)
print(arr)
    
    
    
    