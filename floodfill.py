# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:22:32 2020

@author: kalya
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        color = image[sr][sc]
        image[sr][sc] = newColor
        r = len(image)
        c = len(image[0])
        #print(r,c)
        if sc>0:
            if color == image[sr][sc-1]:
                self.floodFill(image,sr,sc-1,newColor)
        if sr>0:
            if color == image[sr-1][sc]:
                self.floodFill(image,sr-1,sc,newColor)    
        if sc<c-1:
            if color == image[sr][sc+1]:
                self.floodFill(image,sr,sc+1,newColor)
        if sr<r-1:
            if color == image[sr+1][sc]:
                self.floodFill(image,sr+1,sc,newColor)
        
        return image    