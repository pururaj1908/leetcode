# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:48:14 2020

@author: Puru
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        cb = [[0 for j in range(n)] for i in range(n)] 
        def helper(row, count):
            for col in range(n):
                if is_not_under_attack(row, col):
                    move(row, col, "place_queen")
                    if row + 1 == n:
                        count += 1
                    else:
                        count = helper(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    move(row, col, "remove_queen")
            return count
        
        def is_not_under_attack(row,col):
            if cb[row][col] >= 0:
                return True
            else:
                return False
            
        def move(row,col,mtype):
            adder = -1 if mtype == "place_queen" else 1
            cb[row][col] = 1 if mtype == "place_queen" else 0 
            dc = col
            ic = col
            for i in range(row+1,n):
                cb[i][col] += adder 
                if dc-1 >=  0:
                    cb[i][dc-1] += adder
                if ic+1 < n:
                    cb[i][ic+1] += adder
                ic += 1
                dc -= 1
                
        return helper(0,0)    
            
        
        
        