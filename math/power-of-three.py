# Power of Three
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Recursion

"""
This algorithm leverages the fact that $1162261467$ ($3^{19}$) is the largest power of three that fits inside a standard 32-bit signed integer. Because 3 is a prime number, the only positive divisors of $3^{19}$ are strictly other powers of three, meaning any positive $n$ that evenly divides this number must be a power of three. Since it relies on a single arithmetic operation, the solution runs in $O(1)$ time complexity and uses $O(1)$ auxiliary space.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0