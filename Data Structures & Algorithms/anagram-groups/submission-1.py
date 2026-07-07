class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            map1[key].append(s)
        return list(map1.values())