# Minimum Operations to Reduce X to Zero
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Binary Search, Sliding Window, Prefix Sum

"""
The algorithm reframes the problem into finding the longest contiguous subarray with a sum equal to `sum(nums) - x` using a sliding window (two-pointer) approach. It expands the window by incrementing the `right` pointer and contracts it from the `left` whenever the current sum exceeds the target, tracking the maximum valid subarray length. This approach operates in **$O(n)$ time complexity** because each element is visited at most twice, and **$O(1)$ space complexity** since it only uses a few pointers and variables.
"""

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
            
        n = len(nums)
        max_len = -1
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += nums[right]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return n - max_len if max_len != -1 else -1