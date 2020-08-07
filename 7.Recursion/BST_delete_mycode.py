# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:39:51 2020

@author: kalyan
"""
from printBST import binaryTreeToStr
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return binaryTreeToStr(self.root)
    def insertRecursive(self, val):
        self.root = self._insertRecursive(val, self.root)
    
    def _insertRecursive(self, val, curNode):
        if curNode is None:
            return Node(val)
        if curNode.val >  val:
            curNode.left = self._insertRecursive(val, curNode.left)
        else:
            curNode.right = self._insertRecursive(val, curNode.right)
        return curNode
    
    def getIterative(self, val):
        if self.root is None:
            return False
        cur = self.root
        while(cur):
            if cur.val == val:
                return True
            elif cur.val  > val:
                cur = cur.left
            else:
                cur = cur.right
        return False
    def getRecursive(self, val):
        return self._getRecursive(val, self.root)
    
    def _getRecursive(self, val, curNode):
        if curNode is None:
            return False
        if curNode.val == val:
            return True
        elif curNode.val > val:
            return self._getRecursive(val, curNode.left)
        else:
            return self._getRecursive(val, curNode.right)
    def deleteRecursive(self, val):
        self.root = self._deleteRecursive(val, self.root)
    def _deleteRecursive(self, val, curNode):
        if curNode is None:
            return 
        if curNode.val > val:
            curNode.left = self._deleteRecursive(val, curNode.left)
        elif curNode.val < val:
            curNode.right = self._deleteRecursive(val, curNode.right)
        else:
            
            #case 1 -> leaf node return None
            if not curNode.right and not curNode.left:
                return None
            # case 2 -> node has both left and right child
            # find the smallest element in the left sub tree
            elif  curNode.left is not None and curNode.right is not None:
                smallest = self.getsmallest(curNode.right)
                curNode.right = self._deleteRecursive(smallest.val, curNode.right)
                
                smallest.left = curNode.left
                smallest.right = curNode.right
                return smallest
            # case 3-> node has either left child or right child
            else:
                if curNode.left:
                    return curNode.left
                else:
                    return curNode.right
        return curNode
    def getsmallest(self, curNode):
        while(curNode.left):
            curNode = curNode.left
        return curNode

if __name__ == '__main__':
    def makeTree():
        bst = BST()
        bst.insertRecursive(5)
        bst.insertRecursive(3)
        bst.insertRecursive(2)
        bst.insertRecursive(4)
        bst.insertRecursive(8)
        bst.insertRecursive(6)
        bst.insertRecursive(9)
        # bst.insertRecursive(7)
        # bst.insertRecursive(10)
        # bst.insertRecursive(9)
        # bst.insertRecursive(9)
        # bst.root.right.right.right.val = 9
        return bst
    bst = makeTree()
    print(bst)
    bst.deleteRecursive(2)
    print(bst)
    bst.deleteRecursive(3)
    print(bst)
    bst.deleteRecursive(8)
    print(bst)
    bst.deleteRecursive(5)
    # bst.deleteRecursiveDuplicates(2)
    # print(bst)
    # bst.deleteRecursiveDuplicates(3)
    # print(bst)
    # bst.deleteRecursiveDuplicates(8)
    # print(bst)
    # bst.deleteRecursiveDuplicates(5)
    # print(bst)
    # bst.deleteRecursiveDuplicates(9)
    # print(bst)
    # bst.deleteRecursiveDuplicates(9)
    print(bst)
    # bst.deleteRecursiveDuplicates(2)
    # print(bst)
    # bst.deleteRecursiveDuplicates(3)
    # print(bst)
    # bst.deleteRecursiveDuplicates(8)
    # print(bst)
    # bst.deleteRecursiveDuplicates(5)
    # print(bst)
    # bst.deleteRecursiveDuplicates(9)
    # print(bst)
    # bst.deleteRecursiveDuplicates(9)
    # print(bst)

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
