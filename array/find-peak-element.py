# Find Peak Element
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search

"""
This solution uses a **binary search** algorithm to find a peak element by comparing the middle element with its right neighbor. If the middle element is greater than the next, a peak must exist on the left side (including `mid`), so the search space is narrowed to the left half; otherwise, a peak exists on the right side. This approach achieves a **$O(\log n)$ time complexity** and a **$O(1)$ space complexity**.
"""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left