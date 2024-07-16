class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        max_len = 0
        if len(s) == 1:
            return len(s)
        while right < len(s):
            if right == len(s) - 1 and s[right] not in s[left:right]:
                right += 1
                max_len = max(max_len, len(s[left:right]))
            elif s[right] not in s[left:right]:
                right += 1
            else:
                max_len = max(max_len, len(s[left:right]))
                left += 1
                
        return max_len
        
