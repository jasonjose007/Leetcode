# Minimum Moves to Equal Array Elements II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Sorting

"""
This solution solves the problem by finding the median of the array, which is the mathematically optimal value to minimize the sum of absolute differences to all other numbers. It first sorts the array to locate the median at the middle index, and then calculates the total absolute difference between each element and that median. The time complexity is $O(N \log N)$ due to the sorting step, and the space complexity is $O(1)$ auxiliary space (ignoring the space used by the sorting algorithm).
"""

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)