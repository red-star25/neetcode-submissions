import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        
        print(hm)
        maxKey = -math.inf
        maxVal = -math.inf

        for key, value in hm.items():
            if value > maxVal:
                maxVal = value
                maxKey = key
            print("key: ", key, "value: ", value, "maxVal: ", maxVal)
           

        return int(maxKey)