class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                k = j + 1
                l = n - 1

                while k < l:
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        # Skip duplicates for the third and fourth numbers
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1 # Fixed from j to k
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    
                    elif current_sum < target:
                        k += 1
                    else:
                        l -= 1
        
        return res