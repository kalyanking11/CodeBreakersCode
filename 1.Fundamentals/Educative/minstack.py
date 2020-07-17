# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:56:54 2020

@author: kalya
"""

from Stack import MyStack
# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()

class MinStack:
    # Constructor
    def __init__(self):
        # Write your code here
        self.main_stack = MyStack()
        self.min_stack = MyStack()
        # Removes and return value from newStack

    def pop(self):
        # Write your code here
        self.min_stack.pop()
        return self.main_stack.pop()

        # Pushes values into newStack
    def push(self, value):
        # Write your code here
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.top()>value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())

        # Returns minimum value from newStack in O(1) Time
    def min(self):
        # Write your code here
        return self.min_stack.top()

    # Write any helper functions here
