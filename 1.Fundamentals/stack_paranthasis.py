# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:31:27 2020

@author: kalya
"""



    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                #print(top)
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
        