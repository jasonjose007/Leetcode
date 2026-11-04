# Jump Game II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Greedy

"""
This solution uses a **greedy algorithm** to find the minimum number of jumps by keeping track of the farthest reachable index (`farthest`) and the boundary of the current jump (`current_end`). As it iterates through the array, it updates the farthest possible reach and increments the jump count only when the current position reaches the `current_end` boundary. The time complexity is **$O(n)$** because it traverses the list once, and the space complexity is **$O(1)$** as it only uses a few variables for tracking.
"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
                    
        return jumps