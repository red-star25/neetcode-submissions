class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freqMap.items():
            bucket[count].append(num)

        res = []

        for count in range(len(bucket)-1, 0, -1):
            for num in bucket[count]:
                res.append(num)

                if len(res) == k:
                    return res
        
        return []