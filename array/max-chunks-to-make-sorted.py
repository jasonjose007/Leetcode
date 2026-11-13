# Max Chunks To Make Sorted
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Stack, Greedy, Sorting, Monotonic Stack

"""
This solution uses a greedy approach by iterating through the array and tracking the running maximum value (`max_val`) encountered so far. Whenever this running maximum equals the current index `i`, it guarantees that all elements from the beginning up to `i` belong to the same valid chunk (since they consist of numbers from `0` to `i`), allowing the algorithm to increment the chunk count. The time complexity is $O(n)$ because it iterates through the array once, and the space complexity is $O(1)$ as it uses a constant amount of extra memory.
"""

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        max_val = 0
        for i, x in enumerate(arr):
            max_val = max(max_val, x)
            if max_val == i:
                chunks += 1
        return chunks