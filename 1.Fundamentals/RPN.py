# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:51:58 2020

@author: kalya
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i is "+":
                a = stack.pop()
                b = stack.pop()
                
                stack.append(a+b)
            elif i is "-":
                a = stack.pop()
                b = stack.pop()
                
                stack.append(b-a)
            elif i is "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif i is "*":
                a = stack.pop()
                b = stack.pop()
                
                stack.append(a*b)
                
            else:
                stack.append(int(i))
            #print(stack)
        print(stack)        
        return stack[0]