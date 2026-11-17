# Power of Four
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Bit Manipulation, Recursion

"""
This algorithm determines if $n$ is a power of four by using bitwise logic to check if $n$ is positive and has exactly one set bit (`(n & (n - 1)) == 0`), which confirms it is a power of two. It then uses `n % 3 == 1` to distinguish powers of four from other powers of two, leveraging the mathematical property that $4^k \equiv 1 \pmod 3$ whereas $2^{2k+1} \equiv 2 \pmod 3$. Because it relies on a few constant-time mathematical and bitwise operations, the algorithm runs in **$O(1)$ time complexity** and **$O(1)$ space complexity**.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1