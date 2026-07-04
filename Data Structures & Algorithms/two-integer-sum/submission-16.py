class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = collections.defaultdict(int)

        for i in range(len(nums)):
            if (target - nums[i]) not in hm:
                hm[nums[i]] = i
                print(hm)
            else:
                return [hm[target - nums[i]], i]
        
        return []
            
        