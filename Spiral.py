# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 03:13:49 2019

@author: Puru
"""

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        l = []
        c = 0
        k = 0
        i = 0
        j = 0
        while c < m*n:
            
            while j < n - k:
                l.append(matrix[i][j])
                c += 1
                j += 1
                
            j = n - k - 1
            i += 1
            
            while i < m - k:
                l.append(matrix[i][j])                
                c += 1
                i += 1
                
            i = m - k - 1
            j -= 1
            
            while j >= k:
                l.append(matrix[i][j])
                c += 1
                j -= 1
            
            j = k
            i -= 1
            
            while i >= k + 1:
                l.append(matrix[i][j])
                c += 1
                i -= 1
            
            i = k + 1
            j += 1
            
            k += 1
            
        return l
                
s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
        