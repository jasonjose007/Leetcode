# Two Sum II - Input Array Is Sorted
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Two Pointers, Binary Search

"""
This solution uses
 the **two-pointer approach**, initializing one pointer at the beginning and the other at the end of the sorted array, and moving them inward based on how the `current_sum` compares to the `target`. If the sum is too small, the left pointer increases to raise the sum; if it is too large, the right pointer decreases to lower it. This operates in **$O(n)$ time complexity** and **$O(1)$ space complexity** because it iterates through the array at most once using constant extra memory.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1