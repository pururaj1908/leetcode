# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:41:02 2019

@author: Puru
"""
#XOR property :- sum of XORs of all equally spaced numbers will always be 0
#Magic Grid :- Bitwise XOR of all elements in a row or a column must be the same for each row and column
#              Given N is multiple of 4. Print nXn matrix which satisfies above property and exactly contains
#              0 to n^2 - 1 once in matrix 
#              Answer is definitely sorted elements 0 to n^2 - 1 in nXn matrix
class MagicGrid:
    def __init__(self):
        self.N = 0
    def computeMagicGrid(self):
        self.N = int(input())
        matrix = [[0]*self.N for i in range(self.N)]
        x = 0
        for x in range(0,self.N,2):
            for y in range(0,self.N,2):
                
                i += 1
            print("\n")
    def a(self):
        s = 0
        for x in range(19,400,20):
            s = s^x
        
        print(s)    
        
        
        
mg = MagicGrid()
#mg.computeMagicGrid()
mg.a()



            
    
    