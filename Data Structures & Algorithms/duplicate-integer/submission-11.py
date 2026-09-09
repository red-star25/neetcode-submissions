class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valueSet = set()

        for num in nums:
            if num in valueSet:
                return True
            valueSet.add(num)
        
        return False