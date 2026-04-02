class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}

        for n in nums:
            if n not in ans:
                ans[n] = True
            else:
                return True
        return False