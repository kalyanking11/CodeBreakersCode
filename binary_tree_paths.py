# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:55:11 2020

@author: kalya
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return None
        lst = []
        def dfs(root, path):
            if root.left is None and root.right is None:
                lst.append(path)
                print(lst)
            if root.left: dfs(root.left, path+"->"+str(root.left.val))
            if root.right: dfs(root.right,path+"->"+str(root.right.val))
            return lst
        return dfs(root,str(root.val))