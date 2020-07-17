# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 03:29:32 2020

@author: kalya
"""


# Definition for a binary tree node.
# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
            
        lst = []
        def dfs(root,tot):
            if root.left is None and root.right is None:
                lst.append(tot)
                 
                
            if root.left: dfs(root.left,tot+root.left.val)
            if root.right: dfs(root.right,tot+root.right.val)
            return lst
        if sum in dfs(root,root.val):
            return True