class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for idx, i in enumerate(nums):
            ans[i] = idx
        
        for idx, i in enumerate(nums):
            if target - i in ans and ans[target-i] != idx:
                return [idx,ans[target-i]]
        return []