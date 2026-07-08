class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        left = 0
        right = len(s) - 1
        while left <= right:
            lowerLeft = s[left].lower()
            lowerRight = s[right].lower()
            print(lowerLeft,lowerRight)
            if lowerLeft == lowerRight:
                left += 1
                right -= 1
            elif not lowerLeft.isalnum():
                left += 1
            elif not lowerRight.isalnum():
                right -= 1
            else:
                return False

        return True