# Sum of All Subset XOR Totals
# Difficulty: Easy
# Topics: Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_sum = 0
        for num in nums:
            or_sum |= num
        return or_sum << (len(nums) - 1)