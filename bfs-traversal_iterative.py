# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 02:19:21 2019

@author: Puru
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution:
    def levelOrder(self, root):
        
        l = []
        q = []
        i = 0
        if root != None:
            q.append([root,0])
            while q != []:
                element = q.pop(0)
                root = element[0]
                i = element[1]                    
                if root.left != None:
                    q.append([root.left,i+1])
                if root.right != None:
                    q.append([root.right,i+1])
                
                if i>=0 and i < len(l):
                    l[i].append(root.val)
                else:
                    l.insert(i,[root.val])
                
        return l
    

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
    
s = Solution()
print(s.levelOrder(t1))