class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = [] # To store the index of required elements in nums.
        s = {} # To {element : target - element}
        for i in nums:
            s[i] = t-i  # {2:7, 7:2, 11:-2, 15:-6}
        for i in s:
            if s[i] in s.keys():
                l.append(nums.index(s[i]))
        return l
      
