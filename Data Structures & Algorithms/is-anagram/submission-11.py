class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hs = collections.defaultdict(int)

        for char in s:
            hs[char] += 1
        
        for char in t:
            if char in hs:
                hs[char] -= 1
                if hs[char] == 0:
                    del hs[char]

        return len(hs) == 0