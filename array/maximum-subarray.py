# Maximum Subarray
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Divide and Conquer, Dynamic Programming

"""
This solution uses **Kadane's Algorithm** to efficiently find the maximum subarray sum by iterating through the array and deciding at each step whether to add the current element to the existing subarray or start a new one. It operates in **$O(n)$ time complexity** because it traverses the list of $n$ elements once, and uses **$O(1)$ auxiliary space** since it only requires a few variables to track the current and global maximums.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global