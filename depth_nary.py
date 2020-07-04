# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:11:19 2020

@author: kalya
"""



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        return self.helper(root,1)
    def helper(self,root,count):
        if root is None:
            return count
        for i in root.children:
            print(i.val,count)
        #print(self.helper(v,count+1) for v in root.children)
        if root.children:
            return max(self.helper(v,count+1) for v in root.children)
        else: return count
        