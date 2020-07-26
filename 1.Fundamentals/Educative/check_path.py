# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:06:33 2020

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


def check_path(g, source, destination):
    # Write your code here
    visited = [False]*(g.vertices)
    temp = g.array[source].get_head()
    visited[source] = True
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        node = stack.pop()
        if node is destination:
            return True
        temp = g.array[node].get_head()
        while temp is not None:
            
            if visited[temp.data] is False:
                stack.push(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return False


#slight change
def check_path(g, source, destination):
    # Write your code here
    visited = [False]*(g.vertices)
    temp = g.array[source].get_head()
    visited[source] = True
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        node = stack.pop()
        # if node is destination:
        #     return True
        temp = g.array[node].get_head()
        while temp is not None:
            if temp.data == destination:
                return True
            if visited[temp.data] is False:
                stack.push(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return False

#ask doubt
def check_path(g, source, destination):
    # Write your code here
    visited = [False]*(g.vertices)
    return dfs(g, source, destination, visited)

def dfs(g, source, destination, visited):
    if visited[destination] == True:
        return True
    temp = g.array[source].get_head()
    visited[source] = True
    while temp is not None:
        dfs(g, temp.data, destination, visited)
        temp = temp.next_element
    return False

#working_code_recursion
def check_path(g, source, destination):
    # Write your code here
    visited = [False]*(g.vertices)
    visited = dfs(g, source, destination, visited)
    return visited[destination]


def dfs(g, source, destination, visited):
    # if visited[destination] == True:
    #     return True
    temp = g.array[source].get_head()
    visited[source] = True
    while temp is not None:
        visited[temp.data] = True
        dfs(g, temp.data, destination, visited)
        temp = temp.next_element
    return visited



        
        

    
    
    
    

# Make helper functions here
