# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:27:09 2020

@author: kalya
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1.right and not root1.left and not root2.left and not root2.right:
            if root1.val == root2.val:
                return True
            else:
                return False
        
        def helper(root,leaf):
            if root is None:
                return 
            #print(leaf)
            if not root.left and not root.right:
                leaf.append(root.val)
            helper(root.left,leaf)
            helper(root.right,leaf)
            return leaf
        k = helper(root1,[])
        
        l = helper(root2,[])
        print(k,l)
        if k==l:
            return True
        return False
        