class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberHashMap = {}

        for idx,num in enumerate(nums):
            find = target - num
            if find in numberHashMap:
                return [numberHashMap[find], idx]
            numberHashMap[num] = idx
            
        return []