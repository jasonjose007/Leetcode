# Rotate Function
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Dynamic Programming

"""
This solution uses a mathematical sliding-window approach to efficiently compute the rotation function values without recalculating them from scratch. It calculates the initial function value $F(0)$ and the sum of all elements, then iteratively finds subsequent $F(k)$ values in $O(1)$ time by using the relationship $F(k) = F(k-1) + \text{sum} - n \times \text{nums}[n-k]$. The overall time complexity is $O(n)$ to compute the sums and iterate through the rotations, and the space complexity is $O(1)$ since only a few variables are stored.
"""

class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        
        current_f = sum(i * x for i, x in enumerate(nums))
        max_f = current_f
        
        for i in range(1, n):
            current_f = current_f + total_sum - n * nums[n - i]
            if current_f > max_f:
                max_f = current_f
                
        return max_f