class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        else:
            i = 0
            j = min(i + k, len(nums)-1)
            
            while i < len(nums):
                while j > i:
                    if i != j and nums[i] == nums[j] and abs(i-j) <= k:
                        return True
                    j -= 1
                i += 1
                j = min(i + k, len(nums)-1)
        return False