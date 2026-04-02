class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        
        if l == 1:
            return strs[0]
        
        s = sorted(strs)

        res = ""
        for i in range(min(len(s[0]), len(s[-1]))):
            if s[0][i] == s[-1][i]:
                res += s[0][i]
            else:
                break

        return res