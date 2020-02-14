# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:18:09 2019

@author: Puru
"""

class Solution:
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            dp = []
            dp.insert(0,0)
            for i in range(len(nums)):
                dp.insert(i + 1,dp[i] + nums[i])
            print(dp)
            for i in range(len(nums)):
                if dp[i] == (dp[len(nums)] - dp[i+1]):
                    return i
            return -1
            
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
