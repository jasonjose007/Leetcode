# Smallest Stable Index II
# Difficulty: Medium
# Topics: Array, Prefix Sum

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        S = [0] * n
        S[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < S[i + 1]:
                S[i] = nums[i]
            else:
                S[i] = S[i + 1]
        
        curr_max = nums[0]
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            if curr_max - S[i] <= k:
                return i
        return -1