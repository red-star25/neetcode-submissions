class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = res = 0  
        hm = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += hm.get(diff,0)
            hm[curSum] = 1 + hm.get(curSum,0)
        
        return res
