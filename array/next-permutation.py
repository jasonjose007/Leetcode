# Next Permutation
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Two Pointers

"""
This algorithm finds the next lexicographical permutation by first scanning from the right to find the first decreasing element (`i`), swapping it with the smallest element to its right that is larger than it, and then reversing the subarray to the right of `i` to achieve the smallest possible next order. It operates in **$O(n)$ time** complexity by traversing the list a constant number of times and uses **$O(1)$ space** complexity since it modifies the array in-place.
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1