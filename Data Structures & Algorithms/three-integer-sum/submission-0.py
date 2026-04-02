class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                s = nums[idx] + nums[l] + nums[r] 
                if s == 0:
                    res.append([nums[idx],nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+= 1
                    while l < r and nums[r] == nums[r+1]:
                        r-= 1
                
                elif s > 0:
                    r-=1
                
                elif s < 0:
                    l+=1
        

        return res

