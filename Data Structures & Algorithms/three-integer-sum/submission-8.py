class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedArr = sorted(nums)
        # -4,-1,-1,0,1,2
        res = []
        for i in range(0, len(sortedArr) - 2):
            if i > 0 and sortedArr[i] == sortedArr[i - 1]:
                continue
            target  = -sortedArr[i]
            left = i+1
            right = len(sortedArr)-1
            while left < right:
                if sortedArr[left] + sortedArr[right] < target:
                    left += 1
                elif sortedArr[left] + sortedArr[right] > target:
                    right -= 1
                else:
                    res.append([sortedArr[i], sortedArr[left], sortedArr[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedArr[left] == sortedArr[left - 1]:
                        left += 1
                    while right > left and sortedArr[right] == sortedArr[right + 1]:
                        right -= 1
                
        return res