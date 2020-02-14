# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:44:58 2019

@author: Puru
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def postorderTraversal(self, root):
        t = []
        l = []
        
        if root != None:
            while l != [] or root != None:
                if root != None:
                    l.append(root)
                    if root.right != None:
                        l.append(root)
                    root = root.left
                    
                else:
                    root = l.pop()
                    if l != []:
                        if root != l[-1]:
                            t.append(root.val)    
                            root = None
                        else:
                            root = root.right
                        
                    else:
                        t.append(root.val)    
                        root = None
                
                    
        return t

t1 = TreeNode(3)
t2 = TreeNode(1)
t3 = TreeNode(5)
t4 = TreeNode(4)
t5 = TreeNode(2)

t1.left = t2
t2.right = t3
t3.left = t4
t4.right = t5

s = Solution()


print(s.postorderTraversal(t1))