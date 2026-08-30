# Removing Minimum and Maximum From Array
# Difficulty: Medium
# Topics: Array, Greedy

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        min_val = min(nums)
        max_val = max(nums)
        
        i = nums.index(min_val)
        j = nums.index(max_val)
        
        if i > j:
            i, j = j, i
            
        opt1 = j + 1
        opt2 = n - i
        opt3 = (i + 1) + (n - j)
        
        return min(opt1, opt2, opt3)