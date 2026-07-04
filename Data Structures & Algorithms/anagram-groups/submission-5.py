class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(List)

        for s in strs:
            chArr = [0] * 26
            for ch in s:
                chArr[ord(ch) - 97] += 1
            
            if tuple(chArr) not in hm:
                hm[tuple(chArr)] = [s]
            else:
                hm[tuple(chArr)].append(s)

        return list(hm.values())