# Set Mismatch
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Bit Manipulation, Sorting

"""
This solution uses a mathematical approach based on the sum and sum of squares of the first $n$ integers to set up a system of two linear equations. By comparing these expected totals with the actual sum and sum of squares of the input array, it calculates the difference and the sum of the duplicate and missing numbers. Solving this system yields both target numbers in **$O(n)$ time** complexity and **$O(1)$ space** complexity.
"""

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s = n * (n + 1) // 2
        s2 = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = sum(nums)
        actual_sq_sum = sum(x * x for x in nums)
        
        diff = actual_sum - s
        sq_diff = actual_sq_sum - s2
        
        sum_dup_and_missing = sq_diff // diff
        
        dup = (diff + sum_dup_and_missing) // 2
        missing = sum_dup_and_missing - dup
        
        return [dup, missing]