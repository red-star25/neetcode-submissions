class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = {}
        for cs in s:
            if cs not in hm:
                hm[cs] = 0
            hm[cs] += 1
        
        for ct in t:
            if ct in hm:
                hm[ct] -= 1
                if hm[ct] == 0:
                    del hm[ct]

        return len(hm) == 0 
        