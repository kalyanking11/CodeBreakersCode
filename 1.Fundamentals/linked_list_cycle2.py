# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:11:29 2020

@author: kalya
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return
        node = head
        visited = set()
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return