# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:50:42 2020

@author: kalya
"""

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
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key into the trie
    def insert(self, key):
        # None keys are not allowed
        if key is None:
            return

        key = key.lower()  # Keys are stored in lowercase
        current_node = self.root
        index = 0  # To store the character index

        # Iterate the trie with the given character index,
        # If the index points to None
        # simply create a TrieNode and go down a level
        for level in range(len(key)):
            index = self.get_index(key[level])

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")

            current_node = current_node.children[index]

        # Mark the end character as leaf node
        current_node.mark_as_leaf()
        print("'" + key + "' inserted")
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
        
        if current_node.children[index] is None:
            
            continue
        else:
            start = char
            print(start, current_node.children[index])
            
            while current_node.children[index] is not None:
                current_node = current_node.children[index]
                char += 1
                #print(s[char])
                if char<len(s):
                    index = t.get_index(s[char])
                
                    
                    
            if current_node.is_end_word:
                #print(end)
                end = char
                res.append([start, end])
            current_node = t.root
            
    return res
print(find_words("ILIKELEETCODEANDCODEBREAKERS",["LIKE", "CODE", "CODEBREAKERS"]))
        
        
            
            
                    
        
	
