# Surface Area of 3D Shapes
# Difficulty: Easy
# Topics: Array, Math, Geometry, Matrix

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                if val > 0:
                    ans += 4 * val + 2
                    if r + 1 < n:
                        ans -= 2 * min(val, grid[r + 1][c])
                    if c + 1 < n:
                        ans -= 2 * min(val, grid[r][c + 1])
        return ans