# Removing Minimum and Maximum From Array
# Difficulty: Medium
# Topics: Array, Greedy

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        min_val = min(nums)
        max_val = max(nums)
        
        i = nums.index(min_val)
        j = nums.index(max_val)
        
        if i > j:
            i, j = j, i
            
        return min(j + 1, n - i, i + 1 + n - j)