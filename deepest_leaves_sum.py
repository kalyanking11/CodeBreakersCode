# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:11:42 2020

@author: kalya
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return
        height = []
        def dfs(root,h):
            if root.right is None and root.left is None:
                height.append(h)
            
            if root.left:  dfs(root.left,h+1)
            if root.right: dfs(root.right,h+1)
            
            return max(height)
        
        lh = dfs(root,0)
        #print(lh)
        tot = []
        
        def dfs1(root,lh):
            #print(root.val,lh)
            if root is None:
                return 
            if lh == 0:
                tot.append(root.val)
                
            dfs1(root.left,lh-1)
                
            dfs1(root.right,lh-1)
            
            return tot
        
        return sum(dfs1(root,lh))
        