class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        elif len(nums) == 1:
            return nums[0]

        l , h = 0 , len(nums) - 1
        while l <= h:
            m = (l+h)//2
            if m == l:
                return nums[l+1]
            elif nums[m] > nums[l]:
                l = m 
            else:
                h = m
