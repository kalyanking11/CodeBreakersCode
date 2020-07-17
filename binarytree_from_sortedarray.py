# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:11:56 2020

@author: kalya
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(nums):
            
            if not nums:
                return
            root = TreeNode(nums[len(nums)//2])
            root.right = helper(nums[((len(nums)//2)+1):])
            root.left = helper(nums[:len(nums)//2])
            return root
        return helper(nums)