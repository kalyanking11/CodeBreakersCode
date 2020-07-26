# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:59:53 2020

@author: kalyan
"""

class TrieNode:
    def __init__(self, char = ''):
        self.children = {}
        self.freq = 0
        self.char = char
        self.is_end_word = False
    def mark_as_leaf(self):
        self.is_end_word = True
    def unmark_as_leaf(self):
        self.is_end_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
                #print(char+" inserted")
            node = node.children[char]
        node.freq += 1
        node.mark_as_leaf()
    def counter(self):
        lst = []
        #print(self._helper(self.root,'',lst))
        
        return self._helper(self.root,'',lst)
    def _helper(self, node, s, lst):
        #print(node)
        if node.is_end_word:
            lst.append((s,node.freq))
        for char in node.children:
            if char is not None:
                self._helper(node.children[char], s+char, lst)
        return lst
            
        
class Solution(object):
    def topKFrequent(self, words, k):
        t = Trie()
        for word in words:
            t.insert(word)
        #t.counter()
        #print(t)
        #print(t.counter())
        heap = [(-freq, word) for (word,freq) in t.counter()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
        
        
        
        
        
        