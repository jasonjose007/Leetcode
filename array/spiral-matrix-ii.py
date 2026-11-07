# Spiral Matrix II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Matrix, Simulation

"""
This algorithm simulates a clockwise spiral traversal by maintaining four dynamic boundaries (`top`, `bottom`, `left`, `right`) to fill numbers from $1$ to $n^2$ layer by layer. After traversing each edge (left-to-right, top-to-bottom, right-to-left, and bottom-to-top), the corresponding boundary shifts inward until the entire grid is populated. It operates with a time complexity of $O(n^2)$ since each cell is visited once, using $O(1)$ auxiliary space beyond the $O(n^2)$ required for the output matrix.
"""

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while num <= n * n:
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
        return matrix