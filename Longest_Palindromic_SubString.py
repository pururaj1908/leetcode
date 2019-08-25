# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 00:42:58 2019

@author: Puru
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1 :
            return ""
        start = 0; end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i);
            len2 = self.expandAroundCenter(s,i,i + 1);
            lenstr = max(len1,len2)
            if lenstr > end - start :
                start = i - int((lenstr - 1)/2)
                end = i + int(lenstr/2)
        return s[start:end + 1] 
        
    def expandAroundCenter(self,s,left,right):
        L = left
        R = right
        while L>=0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

s = Solution()
print(s.longestPalindrome(input()))    

    
    

        