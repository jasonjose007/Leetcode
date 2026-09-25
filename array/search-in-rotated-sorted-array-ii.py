# Search in Rotated Sorted Array II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search

"""
This solution uses a modified binary search algorithm that accounts for duplicate values by shrinking the search space from both ends (`low` and `high`) when the boundary elements equal the middle element. Otherwise, it identifies which half of the array is normally sorted and determines whether the target falls within that sorted range to appropriately adjust the pointers. The worst-case time complexity is $O(N)$ (occurring when many duplicates force linear pointer adjustments), while the space complexity is $O(1)$.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False