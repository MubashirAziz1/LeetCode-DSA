class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')' , '{':'}' , '[':']'}
        stack = []
        if len(s)%2 != 0:
            return False
            
        i = len(s)-1
        while i >= 0:
            if s[i] not in dic:
                stack.append(s[i])
                i -= 1
            else:
                if len(stack) != 0 and dic[s[i]] == stack[-1]:
                    stack.pop()
                    i -= 1
                else:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True

    
