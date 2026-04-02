class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [*nums]
        # for i in range(len(ans)):
        #     ans.append(ans[i])
        
        # return ans
        ans = []

        for i in range(2):
            for num in nums:
                ans.append(num)
        
        return ans