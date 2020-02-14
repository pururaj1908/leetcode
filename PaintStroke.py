# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:20:35 2020

@author: Puru
"""

class Paint: 

    def __init__(self, row, col, arr): 
        self.ROW = row 
        self.COL = col 
        self.arr = arr

    def visit(self, i, j, visited,ele):
        visited[i][j]=True
        if i + 1 < self.ROW and self.arr[i+1][j] == ele and not visited[i+1][j]:
            self.visit(i+1,j,visited,ele)
        if i - 1 >= 0 and self.arr[i-1][j] == ele and not visited[i-1][j]:
            self.visit(i-1,j,visited,ele)
        if j + 1 < self.COL and self.arr[i][j+1] == ele and not visited[i][j+1]:
            self.visit(i,j+1,visited,ele)
        if j - 1 >= 0 and self.arr[i][j-1] == ele and not visited[i][j-1]:
            self.visit(i,j-1,visited,ele)
    # 2D matrix 
    def count_cells(self): 
        # Make an array to mark visited cells. 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 

        # Initialize count as 0 and travese 
        count = 0
        for i in range(self.ROW): 
            for j in range(self.COL): 
                # If a cell value false then not visited yet 
                # then visit
                if visited[i][j] == False: 
                    # Visit all cells in the array
                    ele = self.arr[i][j]
                    self.visit(i, j, visited, ele)
                    count += 1

        return count 


arr = ["babcaabccbabbbccbabaabcbaba",
"cccaacbbababaccacaacbbaaaaa",
"aabbcbaabaaaaacaaaaacaaabba",
"abaaacaabacaccccaaaaaccaaaa",
"aacacacaaacbaabbbacababacbb",
"acbabbcaabbcccaacaacaabcbba",
"abcacaaaaaaaabcbcbaaaaacaba",
"aaacccbbabaccabaacabaabcaaa",
"aabacbcaaababcacbaaaacbacac",
"bbbbaaacbaaaccccbcacbcbacaa",
"caabaacccacaaabbaaacabaacac",
"aabcbaaacabbacbacabaabacbbc",
"aaabacbaaccbaaabccbcaaaacab",
"aaaaaaaacbaabcabbabcaaabbbc",
"cabbbaacccaaaacbaabaaabaaaa",
"bbbbaaabacacbbaaaccbaaaaaba",
"caacaaaaacbabcabbaccbccaaac",
"acbaaaccaccbaacccacaaaabaab",
"bbccaabaaaababcabbaabccacac",
"bacaaaababcaacaacacbbaaacca",
"ccaaaaababaacacbaaaabaaaaab",
"acabcacaaabaacacacbcbbaacba",
"abccccacaaaabaaaaccbaabaabb",
"cacbcaabbbbaaaacbccababcbaa",
"abaaabaaababbbaaaaababaaaaa",
"aababbcbcaaacbbaaaaaaaaacaa",
"bcacaaccaaacbaaabbbaaaaaaba",
"acaacaaacbbbacbaaaabbaccacc",
"ccbcaccabcacaacccacaaabbaaa",
"caaabacacabbbababbcbcaaaaca",
"acbacacabbababaacaacabacaba",
"cbaccbaaaaaaabaabaccaabccaa",
"bcacacbaaaaccacbbabaabcabca",
"aabccbbcabaababaaaaaaaaaabc",
"acaabacabaaabbcacaacabbcabb",
"aacbaabaaaaabcaaabccaaaabba",
"aabaaccabcaacbbbcbcccbaccba",
"cbaabbababaacbbabbabcaaacab",
"cabbccacabbbaaacacaaabcaaaa",
"cacababbcbbcbcbbacbaabacbaa",
"aacabaaaabbbbbbababaabaaaab",
"caabccaacbaacbbacbbcbabaaaa",
"caccabcbbcaccaccbbbccbcaabc",
"aaaaaacabaccaabcaaacaaacacc",
"cacabacbcaabaababcbbabcacba",
"babaacabaccacbbaacaaaaaaaab",
"bcbcaaaaccaacaaaccaaaacbbac",
"abacacbaacaacaacaaabaabcaca",
"ccaaaacbbbbcabcbbcbcaacabaa",
"caaacaacccbbcbabbbabbaacabc",
"bbabcaacbabacaaaaaabaacabba",
"aabbaaaabbbaaaaaaabbaacaaab",
"caccbabacccaccacabcbbabcaba",
"aacccaabcacaababcabacbacbaa",
"aaabbcababaabaacbcacaaacbaa",
"cabaaaaaaacabacabccccbcbbbb",
"ccabcaabbacbcbaabcbaabbcacc",
"aabbbbcbacbabcbabcacabacbca",
"aacabacaabacbacaaaaabbaccaa",
"ccbbbaaababcaaaabaabbaabacc",
"ccbabacaababaacbbaacbacabca",
"baaacacaabbaaccbccaacbaaaaa",
"bccaacacababbccaaacabcaaaaa",
"caaabcacaaabacabbbababcaabc",
"bacacccaabcbaaaaaaabacaaaba",
"aaaaccacabaccacaabaacbaabcc",
"cbbabacabcbacbbbaaacabaaaaa",
"aacabaacaaaacbcbabcaacacaca",
"aacbacaaacaaaacaabbaaabcbac",
"babaaacacaabaaacaababaabcac",
"bbbaaaababaccaacabaaacaccab",
"abbaaaaacbaccacbaabacabaccb",
"bbbaabaabcbaaaccaaababbcbab",
"abcaaacabccacaaccacbcccaaaa",
"aaaaaccabcaaccaacaaababccca",
"acbcabaabcbbcaaaacbaaccbaab",
"cacccbcabaaaccaaaacbccbbabb",
"cababbbaaabaabacbaaabccbaab",
"caacbcaaaaababaabaabaaacaac",
"abaaaaacacaaabccabaabcaaaca",
"aacaaaaaaaaaabbaccbacbaaacb",
"bcabaabaaacaccbbaabacaacbcc",
"aacaabacaccacaaaaaaacaabacc",
"ccaaacbaabcaacccbacaaaabaaa",
"ccaaabbaaaaaabababbbbaacacc",
"babbaaabcaabbabaaacabbaaaac",
"acacacaacacccbbacacbccccacc",
"aacbcbcccbbbcbaaaaaaaaabaaa",
"baaaaacaaaacbbaacabccaaaabb",
"ababcbbabaaaabaacabbaabcabb",
"aababaaabbacaabcaacbaccbacb",
"caababaaaababaaaabbabbbaaab",
"aaaaaaaccbbbbacaccaccaabacb",
"bacbcbaabaaaaacccacbaccaaac",
"bbacaabaacabbcababacbbcaaca",
"aaaacaaaaaacabababaaccccbac",
"cacccaabacbcbabbcabbaccaaab",
"abacababbccaaaabbcbaaaaaaaa",
"aaacaaacaabaaaacbbbaaabbabc",
"cacaacbbaccacccabcaacacabba"]

row = len(arr) 
col = len(arr[0]) 

p = Paint(row, col, arr) 

print (p.count_cells())
