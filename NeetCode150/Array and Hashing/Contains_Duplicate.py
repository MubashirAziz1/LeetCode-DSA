class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      # Set Data type stores only unique values.
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
