# Perfect Squares
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack

"""
This solution applies **Legendre's Three-Square Theorem**, which states that a number can be expressed as the sum of three squares if and only if it is not of the form $4^k(8m + 7)$; thus, numbers of this specific form return $4$, while all others require at most $3$ squares (checked efficiently by simplifying powers of $4$ and iterating through possible values for the first two squares). The time complexity is $O(\sqrt{n})$ due to the loop searching for two squares, and the space complexity is $O(1)$ since it only uses a few variables.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        
        i = 0
        while i * i <= n:
            j = int((n - i * i) ** 0.5)
            if i * i + j * j == n:
                return (1 if i > 0 else 0) + (1 if j > 0 else 0)
            i += 1
            
        return 3