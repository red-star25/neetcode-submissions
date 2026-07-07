class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = set(nums)
        longest = 0

        for num in hm:
            if(num-1) not in hm:
                length = 1
                while(num+length) in hm:
                    length += 1
                longest = max(length,longest)
        return longest