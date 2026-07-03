class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        nums.sort()
        for right in range(1, len(nums)):
            if nums[left] == nums[right]:
                return True
            left += 1
        
        return False