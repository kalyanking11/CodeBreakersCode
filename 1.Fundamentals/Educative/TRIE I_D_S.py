# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:01:01 2020

@author: kalya
"""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_index(self, t):
        return ord(t) - ord('a')
    def insert(self, key):
        if key is None:
            return
        key = key.lower()
        current_node = self.root
        index = 0
        
        for level in range(len(key)):
            index = self.get_index(key[level])
            
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
            current_node = current_node.children[index]
        current_node.mark_as_leaf()
    def search(self, key):
        if key is None:
            return False
        key = key.lower()
        current_node = self.root
        index = 0
        
        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
        if current_node is not None and current_node.is_end_word():
            return True
        return False
    def has_no_children(self, current_node):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        return True
    def delete_helper(self, key, current_node, length, level):
        deleted_self = False
        if current_node is None:
            return deleted_self
        
        if level is length:
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True
            else:
                current_node.unMarkAsleaf()
                deleted_self = False
        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(
                key, child_node, length, level+1)
            if child_deleted:
                current_node.children[self.get_index(key[level])]
                if current_node.is_end_word:
                    deleted_self = False
                elif self.has_no_children(current_node) is False:
                    deleted_self = False
                else:
                    current_node = None
                    deleted_self = True
            else:
                deleted_self = False
        return deleted_self
        
                