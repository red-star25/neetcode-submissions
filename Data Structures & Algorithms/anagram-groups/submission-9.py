class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for ch in string:
                arr[ord(ch) - ord('a')] += 1
            
            hm[tuple(arr)].append(string)
        print(hm)

        return list(hm.values())

        