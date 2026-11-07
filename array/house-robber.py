# House Robber
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Dynamic Programming

"""
This solution uses a dynamic programming approach to solve the House Robber problem, iterating through the houses and keeping track of the maximum loot possible up to the previous two houses (`prev2`) and the immediate previous house (`prev1`). At each step, it calculates the optimal choice between skipping the current house (`prev1`) or robbing it and adding its value to the loot from two houses ago (`prev2 + num`). The algorithm achieves an optimal **$O(n)$ time complexity** by visiting each house once and an **$O(1)$ space complexity** by only storing variables for the two previous states rather than an entire DP table.
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = 0
        prev1 = 0
        
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1