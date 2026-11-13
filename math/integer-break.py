# Integer Break
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Dynamic Programming

"""
This solution uses a greedy mathematical approach based on the principle that maximizing the product of partitioned integers relies on using as many 3s as possible. It divides $n$ by 3 and handles the remainder (0, 1, or 2) with specific edge cases: if the remainder is 1, it adjusts one 3 into a 4 ($2 \times 2$) to maximize the product. The algorithm runs in $O(\log n)$ time due to exponentiation and requires $O(1)$ auxiliary space.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        quotient, remainder = divmod(n, 3)
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return (3 ** (quotient - 1)) * 4
        else:
            return (3 ** quotient) * 2