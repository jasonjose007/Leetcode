# Arranging Coins
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Binary Search

"""
This solution uses a **mathematical approach** derived from the formula for the sum of the first $k$ integers ($k(k+1)/2 \le n$). By rearranging this inequality into a quadratic equation and solving for $k$ using the quadratic formula, the complete rows can be calculated directly in $O(1)$ time and $O(1)$ space.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        import math
        return int((math.sqrt(8 * n + 1) - 1) // 2)