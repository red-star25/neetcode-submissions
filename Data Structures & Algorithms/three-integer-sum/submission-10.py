class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        res = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                add = nums[i] + nums[j] + nums[k]

                if add == 0:
                    res.append([nums[i], nums[j], nums[k]]) 
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                
                if add > 0:
                    k -= 1
                if add < 0:
                    j += 1
        
        return res