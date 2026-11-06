# Find First and Last Position of Element in Sorted Array
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search

"""
This solution uses Python's built-in `bisect` module to perform two modified binary searches: `bisect_left` to find the first occurrence of the target, and `bisect_right` to find the position just after the last occurrence. After validating that the target actually exists in the array, it returns the start and end indices. The algorithm operates in $O(\log n)$ time complexity and $O(1)$ space complexity.
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        
        left_idx = bisect.bisect_left(nums, target)
        
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        right_idx = bisect.bisect_right(nums, target) - 1
        
        return [left_idx, right_idx]