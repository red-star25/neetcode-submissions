import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        finalstr = regex.sub('', s).lower()

        l = 0
        r = len(finalstr) - 1

        while l < r:
            if finalstr[l] != finalstr[r]:
                return False
            l+=1
            r-=1

        return True