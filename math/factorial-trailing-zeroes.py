# Factorial Trailing Zeroes
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math

"""
This algorithm counts the number of trailing zeroes in $n!$ by determining how many times the prime factor 5 appears in the factorial's prime factorization, since trailing zeroes are formed by pairs of 2 and 5. It iteratively divides $n$ by powers of 5 (accounting for numbers like 25, 125, etc., which contribute multiple factors of 5) and sums the quotients. The time complexity is $O(\log_5 n)$ and the space complexity is $O(1)$.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count