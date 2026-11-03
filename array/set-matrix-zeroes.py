# Set Matrix Zeroes
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Matrix

"""
This solution uses the matrix's own first row and first column as markers to track which rows and columns need to be zeroed out, utilizing a separate boolean variable (`row_zero`) to handle the special case of the first row. By avoiding extra data structures, it achieves an optimal **$O(1)$ space complexity** while running in **$O(m \times n)$ time** by making a few sequential passes over the grid.
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row_zero = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True
                        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
                    
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
                    
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0