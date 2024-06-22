class Solution:
    # For O(n) time complexity, first append the prefixes of elements of an array in result and then multiply the elements
    # of result with postfixes of original elements in array.
    def productExceptSelf(self, nums: List[int]) -> List[int]:     #nums = [1,2,3,4]
        res = [1] *len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix       #res = [1,1,2,6]
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix     #res = [24,12,8,6]
            postfix *= nums[i]
        return res
        
