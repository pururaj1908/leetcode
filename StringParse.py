# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:30:28 2019

@author: Puru
"""

class RegularExpressionMatching:
    def __init__(self,s,p):
        self.s:str = s
        self.p:str = p
    
    def parseString(self):
        if len(self.p) == 0:
            if len(self.s) == 0:
                return True
            else:
                return False
        else:
            lP = len(self.p)
            lS = len(self.s)
            starIndex = self.p.find('*')
            
            if self.p[lP - 1] != '*' and self.p[lP - 1] != '.':
                if self.p[lP - 1] != self.s[lS - 1]:
                    return False
            if self.p[0] != '*' and self.p[0] != '.':
                if lP == 1 or (lP > 1 and self.p[1] != '*'):
                    if self.p[0] != self.s[0]:
                        return False    
     
            # * not there in string
            if starIndex == -1 :
                if lP != lS:
                    return False
                else:
                    for x in range(lS):
                        if lP[x] != lS[x] and lP[x] != '.':
                            return False
            else:
                i = 0
                j = 0
                while i < lS:
                    currentElement = self.s[i]
                    if j < lP:
                        currentParse = self.p[j]
                    else:
                        break
                    # consecutive * case
                    if currentParse == '*':
                        j += 1
                        
                    if j + 1 != lP:
                        lookahead = self.p[j+1]
                        if lookahead == '*':
                            if currentParse != '.':
                                while currentElement == currentParse:
                                    i += 1
                                    currentElement = self.s[i]
                                    
                            
                                
                            j += 1
                            i -= 1
                        else:
                            if currentElement != currentParse and currentParse != '.':
                                return False    
                    j += 1
                    i += 1
                if lP - j > 0:
                    while j < lP:
                        if self.p[j] != '*':
                            if j + 1 < lP:
                                if self.p[j+1] != '*':
                                    return False
                            elif j == lP - 1:
                                return False
                            j += 1
                        j += 1
                            
                        
            return True
            
            
r = RegularExpressionMatching('abcd','a*bc*dg*')
print(r.parseString())
            
            
        