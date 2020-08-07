# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:59:48 2020

@author: kalyan
"""
#          j              i
# a  a  b  a  a  a  a  b  a
# 0  1  2  3  4  5  6  7  8
# 0  1  0  1  2  2  3  4  5

def computeLPSArray(arr, M, lps):
    j = 0
    lps[0] = 0
    i = 1
    while i < M:
        if arr[i] == arr[j]:
            j += 1
            lps[j] = j
            i += 1
        else:
            if j!=0:
                j = lps[j-1]
            else:
                
                lps[i] = 0
                i += 1

def kmp(txt, pat):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0
    computeLPSArray(pat, M, lps)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M :
            print("Patter found at index " + str(i-j))
            j = lps[j-1]
        elif i<N and pat[j]!=txt[i]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
  
if __name__ == "__main__":
	txt = "ABABDABACDABABCABAB"
	pat = "ABABCABAB"
	kmp(txt, pat) 
