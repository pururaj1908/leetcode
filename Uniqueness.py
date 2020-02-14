# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:43:17 2019

@author: Puru
"""
# hack to solve this kind of occurence problem is to make use of hash table which takes each elements' occurance
class Uniqueness:
    def __init__(self):
        self.N = 0
        self.elementList = []
        self.counterList = dict()
        
    def getMinLengthSubStringForUniqueString(self):
        self.N = int(input())
        tmp = str(input()).split(" ")
        for x in range(self.N):
            element = int(tmp[x])
            self.elementList.append(element)
            if element not in self.counterList:
                self.counterList[element] = 1
            else:
                self.counterList[element] += 1
                
        minLength = self.N
        if len(self.counterList) == self.N:
            print(0)
            return
        for i in range(self.N):
          tmpCounterList = self.counterList.copy()
          for j in range(i,self.N):
              tmpCounterList[self.elementList[j]] -= 1
              if tmpCounterList[self.elementList[j]] == 0:
                  tmpCounterList.pop(self.elementList[j])
              
              if len(tmpCounterList) == self.N - j + i - 1:
                  minLength = min(minLength,j-i+1)
                  
        print(minLength)  
      
u = Uniqueness()
u.getMinLengthSubStringForUniqueString()