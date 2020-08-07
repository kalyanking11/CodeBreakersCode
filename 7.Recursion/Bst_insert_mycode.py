# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:33:00 2020

@author: kalyan
"""
# from printBST import binaryTreeToStr
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    # def __str__(self):
    #     return binaryTreeToStr(self.root)
    
    def insertIterative(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            cur = self.root
            prev = None
            isLeft = None
            while (cur):
                prev = cur
                if cur.val > val:
                    isLeft = True
                    cur = cur.left
                else:
                    isLeft = False
                    cur = cur.right
            if isLeft:
                prev.left = Node(val)
            else:
                prev.right = Node(val)
    def insertRecursive(self, val):
        self.root = self._insertRecursive(val, self.root)
    def _insertRecursive(self, val, curNode):
        if curNode is None:
            return Node(val)
        elif curNode.val > val:
            curNode.left = self._insertRecursive(val, curNode.left)
        else:
            curNode.right = self._insertRecursive(val, curNode.right)
        return curNode
if __name__ == '__main__':
    #test cases
    bst = BST()
    bst.insertIterative(5)
    bst.insertIterative(3)
    bst.insertIterative(7)
    bst.insertIterative(2)
    bst.insertIterative(4)
    bst.insertIterative(6)
    bst.insertIterative(8)
    print(bst)

    bst = BST()
    bst.insertRecursive(5)
    bst.insertRecursive(3)
    bst.insertRecursive(7)
    bst.insertRecursive(2)
    bst.insertRecursive(4)
    bst.insertRecursive(6)
    bst.insertRecursive(8)
    print(bst)

            
        
                
