# -*- coding: utf-8 -*-
class Solution:
    def strStr(self, haystack, needle):
        n = len(needle)
        h = len(haystack)
        idx = -1
        if n == 0 or needle == "":
            return 0
        if n <= h:
            if n == h:
                if needle == haystack:
                    return 0
            else:
                i = 0
                j = 0
                for i in range(len(haystack)):
                    if j < len(needle) and needle[j] != haystack[i]:
                        j = 0
                        
                        continue
                    if j == len(needle) - 1:
                        idx = i - j
                        break
                    j += 1
                return idx
        return -1
        
        
s = Solution()
print(s.strStr("aabaaabaaac","aabaaac"))

