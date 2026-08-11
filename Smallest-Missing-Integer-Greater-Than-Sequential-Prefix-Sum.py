# Smallest Missing Integer Greater Than Sequential Prefix Sum
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 0
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        
        s = sum(nums[:i + 1])
        num_set = set(nums)
        while s in num_set:
            s += 1
        return s