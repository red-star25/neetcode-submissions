class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sumEle = 0
        res = math.inf

        for r in range(len(nums)):
            sumEle += nums[r]

            
            while sumEle >= target:
                res  = min(res, r - l + 1)
                sumEle -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0

