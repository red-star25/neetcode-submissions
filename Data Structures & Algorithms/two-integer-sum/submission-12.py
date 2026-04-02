class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for idx, i in enumerate(nums):
            if target - i in hm:
                return [hm[target-i], idx]
            hm[i] = idx        
