class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}

        for i, n in enumerate(nums):
            hs[n] = i

        for i, n in enumerate(nums):
            if target - n in hs and hs[target - n] != i:
                return [i,hs[target-n]]
        return []

        # nums.sort()
        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     add = nums[i] + nums[j]
        #     if add == target:
        #         return [i,j]
        #     elif add > target:
        #         j -=1
        #     elif add < target:
        #         i += 1
        
        # return []



        