# Search a 2D Matrix
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search, Matrix

"""
This solution treats the $m \times n$ 2D matrix as a single, sorted 1D array of length $m \times n$ and performs a standard binary search to locate the target. It maps the 1D binary search index (`mid`) back to 2D matrix coordinates using `mid // n` for the row and `mid % n` for the column. This approach operates with a time complexity of $O(\log(m \cdot n))$ and an auxiliary space complexity of $O(1)$.
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False