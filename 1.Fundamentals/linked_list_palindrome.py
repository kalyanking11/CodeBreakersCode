# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:22:43 2020

@author: kalya
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast: slow = slow.next
        
        while slow and slow.val == rev.val:
            slow = slow.next
            rev = rev.next
        return not slow
            