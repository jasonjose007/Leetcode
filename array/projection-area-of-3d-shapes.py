# Projection Area of 3D Shapes
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math, Geometry, Matrix

"""
This algorithm calculates the total 3D projection area by iterating through the grid once to find the contributions from all three axes: the top view (`xy`), the side view (`yz` using row maxima), and the front view (`zx` using column maxima). It achieves an optimal **$O(N^2)$ time complexity** by visiting each cell in the $N \times N$ grid and an **$O(1)$ space complexity** since it only uses a few variables for tracking maximums and sums.
"""

class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        xy = 0
        yz = 0
        zx = 0
        
        for i in range(n):
            max_row = 0
            max_col = 0
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
            yz += max_row
            zx += max_col
            
        return xy + yz + zx