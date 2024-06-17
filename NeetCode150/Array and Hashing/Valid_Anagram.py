class Solution:
    # My solution (62 ms)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
    # Optimized (51 ms, 17.56 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    
    # The logic is not mine, but the code is written by me. (48 ms, 16.83 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        for i in s:
            if i not in hashmap_s:
                hashmap_s[i] = 1
            else:
                hashmap_s[i] += 1
        
        hashmap_t = {}
        for i in t:
            if i not in  hashmap_t:
                hashmap_t[i] = 1
            else:
                hashmap_t[i] += 1
        if hashmap_s == hashmap_t:
            return True
        else:
            return False
        
    # None (30 ms, 16.91 MB)  
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)