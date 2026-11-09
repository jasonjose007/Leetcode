# Total Hamming Distance
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Bit Manipulation

"""
This solution calculates the total Hamming distance bit by bit, iterating through all 32 bit positions of the integers. For each bit position, it counts how many numbers have a `1` and how many have a `0`, multiplying these counts to find the number of differing pairs at that position and adding it to the total. The time complexity is $O(32n)$ (or $O(n)$) and the space complexity is $O(1)$, where $n$ is the number of elements in `nums`.
"""

class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(32):
            ones = 0
            for x in nums:
                ones += (x >> i) & 1
            zeros = n - ones
            total += ones * zeros
        return total