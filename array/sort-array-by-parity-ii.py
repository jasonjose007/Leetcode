# Sort Array By Parity II
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Two Pointers, Sorting

"""
This solution uses a **two-pointer approach** to scan the array simultaneously for misplaced elements: `i` tracks even indices holding odd numbers, and `j` tracks odd indices holding even numbers. When both pointers find a misplaced element, the algorithm swaps them in place and advances both by two. The time complexity is $O(n)$ since each element is visited at most once, and the space complexity is $O(1)$ because the sorting is done entirely in place without extra data structures.
"""

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        i, j = 0, 1
        n = len(nums)
        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums