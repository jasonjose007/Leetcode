# Unique Paths
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Dynamic Programming, Combinatorics

"""
This solution uses a combinatorial math approach based on the fact that to reach the bottom-right corner from the top-left on an $m \times n$ grid, a robot must take a total of $(m + n - 2)$ moves, exactly $(m - 1)$ of which must be downward. The `math.comb` function calculates the binomial coefficient $\binom{m + n - 2}{m - 1}$, representing the number of ways to choose which moves are down. This approach achieves an optimal time complexity of $O(1)$ and a space complexity of $O(1)$.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)