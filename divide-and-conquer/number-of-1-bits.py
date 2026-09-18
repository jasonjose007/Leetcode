# Number of 1 Bits
# Platform: LeetCode
# Difficulty: Easy
# Topics: Divide and Conquer, Bit Manipulation

"""
This Python solution utilizes the built-in `bit_count()` method, which is implemented in C under the hood to directly count the number of set bits (1s) in the binary representation of the integer `n`. The time complexity is $O(1)$ because the operation executes in constant time relative to the fixed-size integer, and the space complexity is $O(1)$ as it requires no extra memory.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()