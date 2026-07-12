class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitS = s.split(" ")
        if len(splitS) != len(pattern):
            return False

        charToWord = {} 
        wordToChar = {} 

        for c, w in zip(pattern, splitS):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        
        return True