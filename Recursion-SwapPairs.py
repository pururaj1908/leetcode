# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:01:18 2020

@author: Puru
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head):
        def swap(node):
            if node == None or node.next == None:
                return node
            t = node
            node = node.next
            if node.next == None:
                node.next = t
                t.next = None
                return node
            else:
                t.next = swap(node.next)
                node.next = t
                return node
            
            
        if head == None or head.next == None:
            return head
        t = head
        head = head.next
        if head.next == None:
            head.next = t
            t.next = None
        else:
            t.next = swap(head.next)
            head.next = t
        return head
            
        
        
        
        
        
        