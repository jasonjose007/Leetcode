# Kth Smallest Element in a Sorted Matrix
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix

"""
The algorithm performs binary search over the numerical value range between the matrix's minimum and maximum elements (`matrix[0][0]` to `matrix[n-1][n-1]`). In each iteration, it uses a two-pointer technique starting from the bottom-left corner to count elements less than or equal to `mid` in $O(n)$ time, iteratively narrowing the range to find the $k$-th smallest value. This approach runs in $O(n \cdot \log(\text{max} - \text{min}))$ time complexity while requiring only $O(1)$ auxiliary space.
"""

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        def count_less_equal(mid: int) -> int:
            count = 0
            row = n - 1
            col = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        low, high = matrix[0][0], matrix[n - 1][n - 1]
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low