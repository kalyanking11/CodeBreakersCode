# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:39:01 2020

@author: kalyan
"""

class ListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class doublellist:
    def __init__(self):
        self.back = ListNode("back", "back")
        self.front = ListNode("front", "front")
        self.back.next = self.front
        self.front.prev = self.back
        self.countNodes = 0
    #addFront(key,value)
    #removeBack()
    #delete(node)
    
    def delete(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
    
    #back <-> front
    #back <-> 1 <-> front
    #back <-> 1 <-> 2 <-> front
    def addFront(self, key, value):
        new_node = ListNode(key,value)
        print(new_node.value,new_node.key)
        prev_node = self.front.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.front
        self.front.prev = new_node
        return new_node
    
    def removeBack(self):
        key_r = self.back.next.key
        after = self.back.next.next
        self.back.next = self.back.next.next
        self.back.next.prev = self.back
        return key_r
        
        
class LRUCache:
    # back <-> front
    def __init__(self, capacity: int):
        self.lst = doublellist()
        self.capacity = capacity
        self.inCache = {}


    def get(self, key: int) -> int:
        if key in self.inCache:
            
            val = self.inCache[key].value
            self.lst.delete(self.inCache[key])
            newNode = self.lst.addFront(key, val)
            self.inCache[key] = newNode
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.inCache:
            self.lst.delete(self.inCache[key])
            newNode = self.lst.addFront(key, value)
            self.inCache[key] = newNode
            
        else:
            
            newNode = self.lst.addFront(key, value)
            print(newNode)
            self.lst.countNodes += 1
            self.inCache[key] = newNode
            
            
            if self.lst.countNodes > self.capacity:
                key_r = self.lst.removeBack()
                if key_r in self.inCache: 
                    del self.inCache[key_r]
                    self.lst.countNodes -= 1
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)