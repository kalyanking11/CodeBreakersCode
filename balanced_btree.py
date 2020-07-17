# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 03:12:28 2020

@author: kalya
"""


# Definition for a binary tree node.
# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l==-1 or r==-1:
                return -1
            elif abs(l-r)<=1:
                return max(l,r)+1
            else:
                return -1
        res = dfs(root)
        if res == -1:
            return False
        return True
            
            
            
            
        