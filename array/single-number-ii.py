# Single Number II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Bit Manipulation

"""
This solution uses bitwise operations to track the occurrence count of each bit position modulo 3, where `ones` and `zeros` act as a two-bit state machine representing counts of 0, 1, or 2. As it iterates through the array, bits appearing three times are cleared out, leaving only the bits of the single unique number in `ones` at the end. The algorithm runs in $O(n)$ time complexity and $O(1)$ space complexity.
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        zeros = 0
        for num in nums:
            ones = (ones ^ num) & ~zeros
            zeros = (zeros ^ num) & ~ones
        return ones