class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        
        
        for index, i in enumerate(nums):
            ans[index] = i
            ans[index + len(nums)] = i
        
        return ans