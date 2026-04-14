class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for idx, i in enumerate(nums):
            if i not in hm:
                hm[i] = idx
            else:
                if abs(hm[i] - idx) <= k:
                    return True
                hm[i] = idx
        
        return False
        