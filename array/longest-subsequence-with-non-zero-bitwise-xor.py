# Longest Subsequence With Non-Zero Bitwise XOR
# Difficulty: Medium
# Topics: Array, Bit Manipulation

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        zero_count = 0
        for x in nums:
            total_xor ^= x
            if x == 0:
                zero_count += 1
        
        if total_xor != 0:
            return len(nums)
        
        M = len(nums) - zero_count
        if M > 0:
            return len(nums) - 1
        return 0