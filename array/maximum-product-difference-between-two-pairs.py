# Maximum Product Difference Between Two Pairs
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Sorting, Quicksort

"""
This Python solution solves the problem by first sorting the array in ascending order, which places the two smallest numbers at the beginning and the two largest numbers at the end. It then calculates the maximum product difference by multiplying the two largest elements (`nums[-1] * nums[-2]`) and subtracting the product of the two smallest elements (`nums[0] * nums[1]`). The time complexity is $O(n \log n)$ due to the sorting step, and the space complexity is $O(1)$ or $O(n)$ depending on the internal sorting algorithm's memory usage.
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])