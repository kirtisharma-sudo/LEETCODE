class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range (len(nums)):
            self = target - nums[i]
            if self in seen:    
                return [seen[self],i]
            seen[nums[i]]=i
