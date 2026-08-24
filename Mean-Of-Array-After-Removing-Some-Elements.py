# Mean of Array After Removing Some Elements
# Difficulty: Easy
# Topics: Array, Sorting

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n // 20
        trimmed = arr[k : n - k]
        return sum(trimmed) / len(trimmed)