class Solution:
    # Task is to join the elements of a list in a string. (["Hard", "work"] ---->  "Hardwork")
    def encode(self, strs: List[str]) -> str:    
        s = ''
      # s = "4#Hard4#work". Extra terms helpful in indicating the end of the loop when we decode the same string again.
        for i in strs:
            s = s + str(len(i))+'#'+i   
        return s   

    # Task is to split the string into list. ("Hardwork"----> ["Hard", "work"])
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res
