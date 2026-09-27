# Range Sum Query - Immutable
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Design, Prefix Sum

"""
This solution uses a **prefix sum** algorithm, where the `__init__` method precomputes and stores the cumulative sums of the array so that any range sum can be calculated in constant time. The `sumRange` method then answers queries efficiently by subtracting the prefix sum just before the `left` index from the prefix sum at the `right` index. This achieves an **$O(n)$ time and $O(n)$ space complexity** for initialization, and an optimal **$O(1)$ time complexity** for each range query.
"""

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]