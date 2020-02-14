# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:57:18 2019

@author: Puru
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
class Solution:
    
    def buildTree(self,inorder,postorder):
        flag = 0
        root = TreeNode(postorder[len(postorder)-1])
        for i in range(len(inorder)):
            if inorder[i] != postorder[i]:
                flag = 1
                break
        if flag == 0:
            for i in range(1,len(inorder)-1):
                root.left = TreeNode(postorder[len(inorder)-1-i])
                root = root.left
            
        else:
            i = 2
        
        return 