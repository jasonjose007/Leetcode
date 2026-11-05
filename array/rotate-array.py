# Rotate Array
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Two Pointers

"""
This solution uses the **array reversal algorithm**, which rotates the array in place by performing three steps: first reversing the entire array, then reversing the first $k$ elements, and finally reversing the remaining $n - k$ elements. This approach achieves an optimal **$O(n)$ time complexity** by visiting each element a constant number of times and an **$O(1)$ space complexity** because it modifies the array directly without requiring extra memory.
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)