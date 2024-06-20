class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}  # Dictionary to count the occurences of each element.  {1:2, 3:4, 5:1}
        result = [] # Store top K frequent elements. [3,1]
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        # Sort the dict in descending order on the basis of the values/counts.
        sorted_hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True) # [(3, 4), (1, 2), (5, 1)]
        for key,value in sorted_hashmap:
            if len(result) != k:
                result.append(key)
            else:
                break
        return result
