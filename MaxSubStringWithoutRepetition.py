# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:29:04 2019

@author: Puru
"""

class Solution:
    
    def __init__(self):
        self.hashcounter = dict()
    
    def lengthOfLongestSubstring(self, s):
        if s == None:
            return 0
        else:
            maxlength = 0
            tmplength = 0
            start = 0
            for i in range(len(s)):
                currIndex = self.updateHashCounter(s[i],i)
                if currIndex != -1 and currIndex >= start:
                    start = currIndex + 1
                tmplength = i - start + 1
                
                if tmplength > maxlength:
                        maxlength = tmplength
            print(maxlength)
            
    def updateHashCounter(self, c, i):
        s = -1
        if c in self.hashcounter:
            s = self.hashcounter[c]
        self.hashcounter[c] = i
        return s
            
            
                
    
s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
                
