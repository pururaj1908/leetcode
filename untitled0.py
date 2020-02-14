# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:40:49 2020

@author: Puru
"""

def areAlmostEquivalent(s, t):
    # Write your code here
    for i in range(len(s)):
        sd = {}
        td = {}
        for j in s[i]:
            if j in sd:
                sd[j] += 1
            else:
                sd[j] = 1
        for j in t[i]:
            if j in td:
                td[j] += 1
            else:
                td[j] = 1
        
        common = {k: sd[k] for k in sd if k in td and sd[k] == td[k]}
        print(common)
        
areAlmostEquivalent(["aabbcc"],["ggbvv"])