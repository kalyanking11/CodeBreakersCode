# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:17:59 2020

@author: kalya
"""

from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}

# Timed out
def is_tree(g):
    # Write your code here
    return detect_cycle(g) and check_connected(g)
def detect_cycle(g):
    visited = [False]*(g.vertices)
    rec_stack = [False]*(g.vertices)
    for node in range(g.vertices):
        if detect_cycle_rev(g, node, visited, rec_stack):
            return True
    return False
def detect_cycle_rev(g, node, visited, rec_stack):
    if rec_stack[node]:
        return True
    if visited[node]:
        return False
    visited[node] = True
    rec_stack[node] = True
    temp = g.array[node].get_head()
    while temp is not None:
        if detect_cycle_rev(g, temp.data, visited, rec_stack):
            return True
        temp = temp.next_element
    rec_stack[node] = False
    return False

def check_connected(g):
    visited = [False]*(g.vertices)

    visited = check_connected_helper(g, 0, visited)
    for i in visited:
        if not i:
            return False
    return True

def check_connected_helper(g, node, visited):
    
    temp = g.array[node].get_head()
    visited[node] = True
    while temp is not None:
        if not visited[temp.data]:
            check_connected_helper(g, temp.data, visited)
    return visited
        








    
