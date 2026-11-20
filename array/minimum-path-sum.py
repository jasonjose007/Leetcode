# Minimum Path Sum
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Matrix

"""
This solution uses space-optimized dynamic programming to compute the minimum path sum from the top-left to the bottom-right corner of the grid. After initializing a 1D `dp` array with the cumulative sums of the first row, it iterates through the remaining rows, updating each `dp[j]` to the current cell's value plus the minimum of the path from above (`dp[j]`) and the path from the left (`dp[j - 1]`). The algorithm runs in $O(m \times n)$ time to process every cell in the $m \times n$ grid, and uses $O(n)$ space for the 1D `dp` array.
"""

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
            
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                
        return dp[-1]