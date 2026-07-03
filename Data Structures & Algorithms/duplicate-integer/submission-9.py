class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums: #O(n)
            if num not in hm: #O(1)
                hm[num] = 0
            else:
                hm[num] += 1
                if hm[num] >= 1:
                    return True
        print(hm)
        return False

        #O(nlogn) solution
        # left = 0
        # nums.sort() #O(nlogn)
        # for right in range(1, len(nums)): #O(n)
        #     if nums[left] == nums[right]:
        #         return True
        #     left += 1
        
        # return False