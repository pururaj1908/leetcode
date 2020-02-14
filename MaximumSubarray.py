# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:39:12 2019

@author: Puru
"""

class MaximumSubarray:
    def __init__(self,L):
        self.L = L
    
    def computeMaximumSubarray(self):
        maxSum = self.L[0]
        currentSum = self.L[0]
        for x in range(1,len(self.L)):
            
            if currentSum < 0:
                currentSum = self.L[x]
            else:
                currentSum += self.L[x]
            
            
            maxSum = max(maxSum,currentSum)
                
        print(maxSum)

ms = MaximumSubarray([2,1,-3,4,-1,2,1,-5,4])
ms.computeMaximumSubarray()
                    
                    

            
                
         
                
                
                                
                
            