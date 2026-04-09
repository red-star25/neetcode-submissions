class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1

            if len(hm) <= 2:
                continue
            
            new_count = defaultdict(int)
            for n, c in hm.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count
        
        res = []
        for n in hm:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res
            