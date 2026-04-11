class Solution:
    def alphaNum(self, s: str) -> bool:
        return (
            ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9')
        )
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            if self.alphaNum(s[i]) and self.alphaNum(s[j]):
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                if not self.alphaNum(s[i]):
                    i += 1
                if not self.alphaNum(s[j]):
                    j -= 1
        return True