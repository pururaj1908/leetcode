# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:14:07 2020

@author: Puru
"""

class Solution:
    def minSumPseudoBinary(self,n):
        while n > 0:
            tmp = n
            m = 0
            p = 1
            while tmp != 0:
                r = tmp % 10;
                tmp = tmp // 10;
                if r != 0:
                    m += p
                p *= 10
            print(m,end=' ')
            n = n - m

s = Solution()
s.minSumPseudoBinary(452)
                    