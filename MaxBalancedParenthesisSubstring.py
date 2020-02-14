# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 03:30:21 2019

@author: Puru
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        currentLength = 0
        parenthesisStack = []
        intermediateStack = []
        
        for c in s:
            if c == ')':
                if len(parenthesisStack) == 0:
                    parenthesisStack.append(c)
                    currentLength = 0
                else:                
                    if parenthesisStack[-1] == ')':
                        parenthesisStack.append(c)
                        currentLength = 0
                    else:
                        parenthesisStack.pop()
                        currentLength += 2
            else:
                parenthesisStack.append(c)
                intermediateStack.append(currentLength)
                currentLength = 0
            
            maxLength = max(maxLength,currentLength)
        return maxLength
        
 
                        
                
            
            
s = Solution()
print(s.longestValidParentheses('()(()'))
    
                
                
    