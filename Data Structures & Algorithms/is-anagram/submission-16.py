class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {}

        for ch in s:
            charMap[ch] = 1 + charMap.get(ch, 0)
        
        for ch in t:
            if ch in charMap:
                charMap[ch] -= 1
                if charMap[ch] == 0:
                    del charMap[ch]
        
        return len(charMap) == 0
        