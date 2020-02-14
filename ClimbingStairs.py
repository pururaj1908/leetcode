# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:48:18 2019

@author: Puru
"""

class ClimbingStairs:
    def climbStairs(self,n):
        a = 1
        b = 1
        c = 0
        if n == 0 or n == 1:
            return 1
        for x in range(2,n+1):
            c = a + b
            a = b
            b = c
        
        
        return c
        