# Sort Colors
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Two Pointers, Sorting, Quicksort, Bubble Sort

"""
This solution uses the **Dutch National Flag algorithm** (three-way partitioning), which utilizes three pointers (`low`, `mid`, and `high`) to sort the array in a single pass by swapping `0`s to the beginning, `2`s to the end, and leaving `1`s in the middle. It runs in **$O(n)$ time complexity** because the array is traversed linearly, with each element examined at most twice. The auxiliary **space complexity is $O(1)$** as the sorting is performed entirely in-place.
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1