class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left , right = 0 , 0
        res = 0
        dic = {}
        while right < len(s):
            dic[s[right]] = 1 + dic.get(s[right] , 0)
            if (right-left+1) - max(dic.values()) <= k:
                res = max(res, right-left+1)
            else:
                dic[s[left]] -= 1
                left += 1
            right += 1
        return res
            
        
