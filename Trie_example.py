# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:52:16 2020

@author: kalyan
"""
class TrieNode:
    def __init__(self, char = ''):
        self.children = [None]*26
        self.is_end_word = False
        self.char = char
    def mark_as_leaf(self):
        self.is_end_word = True
    def un_mark_as_leaf(self):
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_index(self,t):
        return ord(t) - ord('a')
    def insert(self, key):
        if key is None:
            return
        key = key.lower()
        current_node = self.root
        index = 0
        
        for char in range(len(key)):
            index = self.get_index(key[char])
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[char])
        current_node = current_node.children[index]
        current_node.mark_as_leaf()
def find_words(s, arr):
    t = Trie()
    s = s.lower()
    res = []
    for word in arr:
        t.insert(word)
    current_node = t.root

    for char in range(len(s)):
        index = t.get_index(s[char])
        
        print("k "+ s[char],index)
        print(current_node.children[index])
        if current_node.children[index] is None:
            print("Not Found")
            continue
        else:
            start = char
            print(start)
            while current_node.children[index] is not None:
                current_node = current_node.children[index]
                char += 1
                print(s[char])
                index = t.get_index(s[char])
                
                
            if current_node.is_end_word:
                #print(end)
                end = char
                res.append([start, end])
            else:
                current_node = t.root
                
            
                
                
                
                
        
        
        
        
    return res
print(find_words("ILIKELEETCODEANDCODEBREAKERS",["LIKE", "CODE", "CODEBREAKERS"]))
        
        
            
            
                    
        
	
