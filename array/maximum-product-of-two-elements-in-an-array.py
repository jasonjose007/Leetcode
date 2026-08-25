# Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Topics: Array, Sorting, Heap (Priority Queue)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
        return (max1 - 1) * (max2 - 1)