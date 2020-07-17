# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:16:12 2020

@author: kalya
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        d =dummy
        c =0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            s = a + b + c
            c = 0
            
            if s > 9:
                c = 1
                s = s%10
            d.next = ListNode(s)
            d = d.next
            if l1 : l1 =l1.next
            if l2 : l2 =l2.next
        
        if c>0:
            d.next = ListNode(c)
        return dummy.next