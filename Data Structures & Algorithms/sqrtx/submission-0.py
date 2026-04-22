class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        
        while l <= r:
            mid = (l + r) // 2

            if mid*mid < x:
                l = mid + 1
            elif mid*mid > x:
                r = mid - 1
            elif mid*mid == x:
                return mid
       

        return r