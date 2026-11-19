# Minimum Score by Changing Two Elements
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Greedy, Sorting

"""
The algorithm first sorts `nums` so it can find the minimum possible range (high score) by testing the three optimal ways to change two elements: modifying the two smallest, the two largest, or one from each end. Changing those elements to match remaining values guarantees the minimum pairwise difference (low score) becomes `0`, leaving the smallest remaining range among `nums[-1] - nums[2]`, `nums[-2] - nums[1]`, and `nums[-3] - nums[0]` as the total minimum score. Sorting dominates the complexity, taking $O(n \log n)$ time and $O(n)$ auxiliary space (due to Python's Timsort).
"""

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])