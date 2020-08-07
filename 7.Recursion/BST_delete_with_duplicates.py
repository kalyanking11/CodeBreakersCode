# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:02:23 2020

@author: kalyan
"""
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
    def deleteRecursivewithdup(self, val):
        self.root = self._deleteRecursivewithdup(val, self.root)
    def _deleteRecursivewithdup(self, val, curNode):
        if curNode is None:
            return 
        if curNode.val > val:
            curNode.left = self._deleteRecursivewithdup(val, curNode.left)
        elif curNode.val < val:
            curNode.right = self._deleteRecursivewithdup(val, curNode.right)
        else:
            
            #case 1 -> leaf node return None
            if not curNode.right and not curNode.left:
                return None
            # case 2 -> node has both left and right child
            # find the smallest element in the left sub tree
            elif  curNode.left is not None and curNode.right is not None:
                smallest = self.getsmallestanddelete(curNode.right,curNode)
                
                
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
    def getsmallestanddelete(self, curNode, prev):
        while(curNode.left):
            prev = curNode
            curNode = curNode.left
        if prev.left is curNode:
            prev.left = curNode.right
        else:
            prev.right = curNode.right
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
        bst.insertRecursive(7)
        bst.insertRecursive(10)
        bst.insertRecursive(9)
        bst.insertRecursive(9)
        bst.root.right.right.right.val = 9
        return bst
    bst = makeTree()
    print(bst)
    bst.deleteRecursivewithdup(2)
    print(bst)
    bst.deleteRecursivewithdup(3)
    print(bst)
    bst.deleteRecursivewithdup(8)
    print(bst)
    bst.deleteRecursivewithdup(5)
    print(bst)
    bst.deleteRecursivewithdup(9)
    print(bst)
    bst.deleteRecursivewithdup(9)
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