class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [*nums]
        for i in range(len(ans)):
            ans.append(ans[i])
        
        return ans