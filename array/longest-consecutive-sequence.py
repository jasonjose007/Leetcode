# Longest Consecutive Sequence
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Union-Find

"""
This algorithm stores the numbers in a hash set and identifies the start of a potential sequence by checking if `n - 1` does not exist in the set. For each sequence start, it iteratively increments a counter as long as `n + length` is present in the set to determine the sequence's total length and track the maximum. Because each number is visited at most twice, the solution achieves an optimal **$O(n)$ time complexity** and uses **$O(n)$ space complexity** to store the set.
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest