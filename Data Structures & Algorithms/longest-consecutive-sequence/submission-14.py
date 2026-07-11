class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = set(nums)

        res = 0
        for i in nums:
            count = 1
            j = i
            while j - 1 in hm: 
                count += 1
                j -= 1 
            res = max(count, res)
        
        return res