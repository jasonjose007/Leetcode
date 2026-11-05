# Ugly Number
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math

"""
This solution determines if a number is ugly by iteratively dividing the input $n$ by its prime factors 2, 3, and 5 as long as it is evenly divisible by them. If the remaining value of $n$ reduces to 1, it confirms that no other prime factors exist, returning `true`; otherwise, it returns `false`. The time complexity is $O(\log n)$ because $n$ is divided by at least 2 in each step, and the space complexity is $O(1)$ since it only uses a constant amount of extra memory.
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1