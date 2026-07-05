class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: #[7]
            return [nums[0]] 
        
        hm = collections.defaultdict(int)

        for num in nums: # O(n)
            hm[num] += 1
        
        sorted_hm = dict(sorted(hm.items(), key=lambda item:item[1], reverse=True))

        res = []
        print(sorted_hm.keys())

        for num in range(0,k):
            res.append(list(sorted_hm.keys())[num])

        print(res)
        return res
        
