# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:37:03 2020

@author: kalya
"""


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return
        slow = fast = head
        
        while fast.next is not None:
            
            slow = slow.next
            if fast.next.next is None :
                return False
            fast = fast.next.next
            if slow is fast:
                return True
            
        
        return False