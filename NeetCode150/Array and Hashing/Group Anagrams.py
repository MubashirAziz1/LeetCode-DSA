from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            hashmap[key].append(i)
        return list(hashmap.values())
