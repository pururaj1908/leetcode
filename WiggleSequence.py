# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:47:15 2020

@author: Puru
"""

class Solution:
    def wiggleMaxLength(self, nums):
        l = []
        if len(nums) < 2:
            return len(nums)
        l.append([nums[0],1,-1])
        m = 1
        for i in range(1,len(nums)):
            f = 0
            l = list(filter(lambda r:r[1] == m,l))
            for x in l:
                if x[2] == -1:
                    if nums[i] > x[0]:
                        x[0] = nums[i]
                        x[1] += 1
                        x[2] = 0
                        f = 1
                    elif nums[i] < x[0]:
                        x[0] = nums[i]
                        x[1] += 1
                        x[2] = 1
                        f = 1
                elif x[2] == 0 and nums[i] < x[0]:
                    x[0] = nums[i]
                    x[1] += 1
                    x[2] = 1
                    f = 1
                elif x[2] == 1 and nums[i] > x[0]:
                    x[0] = nums[i]
                    x[1] += 1
                    x[2] = 0
                    f = 1
            if f == 1:
                m += 1
                l = list(filter(lambda r:r[1] == m,l))
            else:
                l.append([nums[i],m,l[0][2]])
            
        return m
            
                    
s = Solution()
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
                    
                    
            
            

        
            
                
        