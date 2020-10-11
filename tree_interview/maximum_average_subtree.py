# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:51:49 2020

@author: kalya
"""

class EmployeeNode:
    def __init__(self, tenure, children):
        self.tenure = tenure
        self.children = children
        
class Solution:
    total = 0
    def dfs(self, root, c):
        print(root)
        if root.children is None:
            return (0,c)
        l = [self.dfs(emap[node],c+1)[0] for node in root.children]
        return (root.tenure + sum(l), c+len(l))
    
    def emp(self, employees):
        global emap
        emap = {e.tenure:e for e in employees}
        print(self.dfs(employees[0],1))
        print(self.dfs(employees[1],1))
        print(self.dfs(employees[2],1))
        print(self.dfs(employees[3],1))

if __name__ == "__main__":
    s = Solution()
    #s.emp([EmployeeNode(20,[12,18]), [12,[11,2,3]], [18,[15,8]]])
    a = EmployeeNode(20,[12,18])
    b = EmployeeNode(12,[11,2,3])
    c = EmployeeNode(18,[15,8])
    d = EmployeeNode(11,[])
    e = EmployeeNode(2,[])
    f = EmployeeNode(3,[])
    g = EmployeeNode(8,[])
    h = EmployeeNode(15,[])
    
    print(a.tenure)
    s.emp([a,b,c,d,e,f,g,h])
    
        
            