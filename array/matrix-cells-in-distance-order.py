# Matrix Cells in Distance Order
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math, Geometry, Sorting, Matrix

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        max_dist = max(rCenter, rows - 1 - rCenter) + max(cCenter, cols - 1 - cCenter)
        buckets = [[] for _ in range(max_dist + 1)]
        for r in range(rows):
            dr = abs(r - rCenter)
            for c in range(cols):
                buckets[dr + abs(c - cCenter)].append([r, c])
        res = []
        for b in buckets:
            res.extend(b)
        return res