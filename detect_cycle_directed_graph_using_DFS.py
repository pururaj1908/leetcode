# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:36:49 2019

@author: Puru
"""
#for connected graphs
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addDirectedEdge(self,u,v):
        self.graph[u].append(v)
    
    def dfs(self,vis,stack,u):
        vis[u] = 1
        stack[u] = 1
        
        if u in self.graph:
            for v in self.graph[u]:
                if vis[v] != 1:
                    if self.dfs(vis,stack,v) == True:
                        return True
                elif stack[v] == 1:
                    return True
        stack[u] = -1
        return False
        
    def isCyclic(self):
        vis = [-1] * self.V
        stack = [-1] * self.V        
        isCycle = False
        for u in self.graph:
            if vis[u] != 1:
                if self.dfs(vis,stack,u) == True:
                    isCycle = True
                    break
                    
        if isCycle == True:
            print("Cycle found")
            
        else:
            print("Cycle not found")
                
                
g=Graph(4) 
g.addDirectedEdge(0, 1) 
g.addDirectedEdge(0, 2) 
g.addDirectedEdge(1, 2) 
g.addDirectedEdge(2, 0) 
g.addDirectedEdge(2, 3) 
g.addDirectedEdge(3, 3)
g.isCyclic()