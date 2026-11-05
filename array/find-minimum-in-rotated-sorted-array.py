# Find Minimum in Rotated Sorted Array
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search

"""
This solution uses a modified **binary search** algorithm by maintaining two pointers, `left` and `right`, to repeatedly narrow down the search space. By comparing the middle element (`nums[mid]`) with the rightmost element (`nums[right]`), it determines which half of the array contains the pivot (the minimum element) and adjusts the pointers accordingly until they converge. The time complexity is **$O(\log n)$** because the search space is halved in each iteration, and the space complexity is **$O(1)$** as it only uses a constant amount of extra memory for pointers.
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]