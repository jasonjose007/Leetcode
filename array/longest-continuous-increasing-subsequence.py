# Longest Continuous Increasing Subsequence
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array

"""
This solution uses a **greedy linear scan** approach, iterating through the array once while maintaining the length of the current strictly increasing subsequence (`curr_len`) and updating the overall maximum length (`max_len`) whenever a larger sequence is found. If the current element is not greater than the previous one, the streak is broken and `curr_len` resets to 1. The algorithm runs in **$O(n)$ time** (where $n$ is the number of elements in `nums`) and requires **$O(1)$ space** by using only a constant number of variables.
"""

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        curr_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                curr_len = 1
                
        return max_len