# The K Weakest Rows in a Matrix
# Difficulty: Easy
# Topics: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_ones(row: List[int]) -> int:
            low, high = 0, len(row)
            while low < high:
                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        strengths = [(count_ones(row), i) for i, row in enumerate(mat)]
        strengths.sort()
        return [i for _, i in strengths[:k]]