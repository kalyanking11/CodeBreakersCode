# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:14:22 2020

@author: kalya
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getlen(self,node):
        lenn = 0
        while(node.next is not None):
            lenn+=1
            node=node.next
        return lenn
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        lena = self.getlen(headA)
        lenb = self.getlen(headB)     
        diff = lena - lenb
        #print(lena,lenb) 
        if diff > 0:
            for i in range(diff):
                headA = headA.next
                
        elif diff<0:
            for i in range(abs(diff)):
                headB = headB.next
                #print(1)
        #print(headA,headB)        
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            