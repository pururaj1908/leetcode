# To minimize the number of letters "R" in the essay and to have minimum length of such essay

def countR(word):
    cR = 0
    for x in word:
        if x == 'r':
            cR = cR + 1
    return cR

class FedorAndEssay:
    
    m = 0
    n = 0
    syndictionary = dict()
    wordList = []
    counters = [0,0]
    
    def preProcessingInputData(self):    
        self.m = int(input())
        words = str(input()).lower()
        self.n = int(input())
        
        for x in range(self.n):
            tmpsynpair = str(input()).lower().split(' ')
            if tmpsynpair[0] in self.syndictionary:
                self.syndictionary[tmpsynpair[0]] = self.syndictionary[tmpsynpair[0]] + [tmpsynpair[1]]
            else:
                self.syndictionary[tmpsynpair[0]] = [tmpsynpair[1]]
                        
        self.wordList = words.split(' ');
        print(self.syndictionary)
        
    def optimumRLetteredWordOrMinLengthWord(self,word):
        
        wordStackAlreadyTraversed = []
        rMinWordsStack = [word]
        rMinCount = countR(word)
        returnWord = word        
        while word in self.syndictionary and word not in wordStackAlreadyTraversed:
            wordStackAlreadyTraversed.append(word)
            synwordList = self.syndictionary[word]
            for synword in synwordList:
                if countR(synword) < rMinCount:
                    rMinCount = countR(synword)
                    rMinWordsStack.clear()
                    rMinWordsStack.append(synword)                    
                else:
                    if countR(synword) == rMinCount:
                        rMinWordsStack.append(synword)                
                word = synword
            
        minLengthOptimalWord = len(rMinWordsStack[0])
        returnWord = rMinWordsStack[0]
        for minRWords in rMinWordsStack:
            if len(minRWords) < minLengthOptimalWord:
                returnWord = minRWords
            
        return returnWord
                                        
    def optimizeEssay(self):
        for i in range(len(self.wordList)):
            synword = self.optimumRLetteredWordOrMinLengthWord(self.wordList[i])
            self.counters[0] += countR(synword)
            self.counters[1] += len(synword)
            
            if self.wordList[i] in self.syndictionary and self.syndictionary[self.wordList[i]] != synword :
                self.syndictionary[self.wordList[i]] = synword
                
        print(self.counters[0],self.counters[1])
        
fde = FedorAndEssay()
fde.preProcessingInputData()
fde.optimizeEssay()


