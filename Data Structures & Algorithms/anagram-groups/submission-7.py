class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)

        for s in strs:
            chArr = [0] * 26
            for ch in s:
                chArr[ord(ch) - 97] += 1
            
            hm[tuple(chArr)].append(s)

        return list(hm.values())