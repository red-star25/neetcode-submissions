class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        
        res = []

        for key, value in hm.items():
            if hm[key] > len(nums) // 3:
                res.append(key)
        
        print(res)

        return res