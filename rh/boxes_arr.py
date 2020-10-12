# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:29:22 2020

@author: kalyan
"""

def rectangle(operations):
    boxes = []
    
    res = []
    
    for op in operations:
        
        if op[0] == 0:
            boxes.append((op[1], op[2]))
            
        elif op[0] == 1:
            temp = []
            for box in range(0, len(boxes)):
            
                if ((boxes[box][0] <= op[1] and boxes[box][1] <= op[2]) or \
                    (boxes[box][0] <= op[2] and boxes[box][1] <= op[1])):
                        temp.append(True)
                        
                else:
                    temp.append(False)
                #print(temp)
            res.append(all(temp))
                
                
    return res

print(rectangle([[0,1,3],[0,4,2],[1,3,4],[1,3,2]]))

                
            
                    
                
                
                
         
            