# Maximum Product of Three Numbers
# Difficulty: Easy
# Topics: Array, Math, Sorting

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        import heapq
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2, nums)
        return max(largest[0] * largest[1] * largest[2], smallest[0] * smallest[1] * largest[0])