class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s1 = defaultdict(int)
        for i in s:
            s1[i] += 1
        
        s2 = defaultdict(int)
        for i in t:
            s2[i] += 1

        print(s1)
        print(s2)
        
        for idx, i in enumerate(s1):
            if s2[i] != s1[i]:
                return False
        
        return True
