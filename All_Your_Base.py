# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:54:54 2020

@author: Puru
"""

class Solution:
    def allyourbase(self,s):
        d = {}
        c = 0
        d[s[0]] = 1
        for i in range(1,len(s)):
            if s[i] not in d:
                if c == 0:
                    d[s[i]] = c
                    c += 2
                else:
                    d[s[i]] = c
                    c += 1
                    
        result = ""
        for x in s:
            result += str(d[x])
               
        base10 = 0
        i = len(result) - 1
        j = 0
        while i >= 0:
            base10 += (int(result[i])) * (c**j)
            i -= 1
            j += 1
            
        return base10
        

s = Solution()
n = s.allyourbase('11001001')
print(n)
        
    
            
            
                    
        