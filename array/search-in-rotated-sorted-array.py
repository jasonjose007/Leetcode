# Search in Rotated Sorted Array
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search

"""
This algorithm uses a **modified binary search** that identifies which half of the array is properly sorted at each iteration (`left` to `mid` or `mid` to `right`). It then checks if the `target` falls within the boundaries of that sorted half to decide whether to discard the left or right portion of the search space. This achieves an optimal time complexity of **$O(\log n)$** while requiring **$O(1)$** auxiliary space.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1