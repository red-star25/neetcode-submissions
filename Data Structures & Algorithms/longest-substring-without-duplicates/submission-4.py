class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            curr_char = s[end]

            if curr_char in char_map and char_map[curr_char] >= start:
                start = char_map[curr_char] + 1
            
            char_map[curr_char] = end

            max_length = max(max_length, end - start + 1)
        
        return max_length