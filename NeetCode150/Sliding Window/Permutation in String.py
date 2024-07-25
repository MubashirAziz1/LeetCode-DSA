class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1count , s2count = {} , {}
        n = len(s1)

        for i in s1:
            s1count[i] = 1 + s1count.get(i,0)
        
        for i in range(n):
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)
        
        l , r = 0 , n-1
        while r < len(s2):
            if s1count == s2count:
                return True
            else:
                if r == len(s2) - 1:
                    if s1count == s2count:
                        return True
                    else:
                        return False
            
                r += 1
                if s2[r] in s2count:
                    s2count[s2[r]] += 1
                else:
                    s2count[s2[r]] = 1
                
                s2count[s2[l]] -= 1
                if s2count[s2[l]] == 0:
                    del s2count[s2[l]]
                
                l += 1
        return False
