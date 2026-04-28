class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = defaultdict(int)

        for ch in s:
            hm[ch] += 1
        
        for ch in t:
            if ch in hm:
                hm[ch] -= 1
                if hm[ch] <= 0:
                    del hm[ch]

        return len(hm) == 0
                