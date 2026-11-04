# Range Addition II
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math

"""
Since every operation increments a submatrix rooted at the top-left corner $(0,0)$, the maximum integers will always reside in the overlapping region shared by all operations. The algorithm finds the dimensions of this overlap by taking the minimum row size and minimum column size across all operations, returning their product as the count of maximum integers (or $m \times n$ if no operations are given). This approach operates in $O(k)$ time complexity, where $k$ is the number of operations, and uses $O(1)$ auxiliary space.
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops:
            return m * n
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        return min_a * min_b