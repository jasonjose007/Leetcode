# Summary Ranges
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array

"""
This solution uses a **
two-pointer (or streak-tracking) approach** by iterating through the sorted array to find contiguous ranges of numbers where each element increments by 1. Whenever a sequence breaks, it records the range as either a single number or an "start->end" string into the result list. The time complexity is **$O(n)$** because it traverses the list of $n$ elements at most twice, and the space complexity is **$O(1)$** auxiliary space (excluding the output array).
"""

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")
            i += 1
        return ans