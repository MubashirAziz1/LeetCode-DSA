def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        longest_s = 1
        counter = 1
        for i in range(len(nums)):
            if i <len(nums)-1:
                
                if nums[i+1] - nums[i] == 1:
                    counter += 1
                else:
                    if longest_s<=counter:
                       longest_s = counter
                    counter = 1
            else:
                if longest_s<=counter:
                    longest_s = counter
                
        return longest_s
            
