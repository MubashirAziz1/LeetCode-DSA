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
            length = int(s[i])
            res.append(s[i+2 : i+2+length])
            i = i+2+length
        return res
