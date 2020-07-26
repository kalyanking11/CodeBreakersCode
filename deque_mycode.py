# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:13:06 2020

@author: kalyan
"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
class Deque:
    # head <-> tail
    def __init__(self):
        self.size = 0
        self.head = ListNode('head')
        self.tail = ListNode('tail')
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return self.size
    
    def addFirst(self, item):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 2 <-> 1 <-> tail
        new_node = ListNode(item)
        prev_first = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = prev_first
        prev_first.prev = new_node
        self.size += 1
    
    def addLast(self,item):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 1 <-> 2 <-> tail
        new_node = ListNode(item)
        prev_last = self.tail.prev
        prev_last.next = new_node
        new_node.next = self.tail
        new_node.prev = prev_last
        self.tail.prev = new_node
        
        self.size += 1
    
    def removeFirst(self):
        # head <-> tail
        # head <-> 1 <-> 2 <-> tail
        # head <-> 2 <-> tail
        if self.isEmpty():
            return
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        
    def removeLast(self):
        # head <-> tail
        # head <-> 1 <-> 2 <-> tail
        # head <-> 1 <-> tail
        if self.isEmpty():
            return
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
    def asList(self):
        res = []
        cur = self.head.next
        while cur is not self.tail:
            res.append(cur.val)
            cur =cur.next
        return res
    

if __name__ == '__main__':
    #test cases
    dq = Deque()
    for i in range(1,6):
        dq.addFirst(i)
    for i in range(6,15):
        dq.addLast(i)

    # 5,4,3,2,1,6,7,8,9,10
    print(dq.asList())
    dq.removeFirst()
    print(dq.asList())
    #4,3,2,1,6,7,8,9,10
    dq.removeLast()
    print(dq.asList())
    #4,3,2,1,6,7,8,9
            
        
        
        
        
    
        
