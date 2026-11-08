# Smallest Range I
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math

"""
The algorithm finds the minimum and maximum values in the array and attempts to shrink their difference by adding or subtracting up to $k$ from each, effectively reducing the total spread by $2k$. If the adjusted spread is still positive, that value is returned; otherwise, it returns $0$ since the range can be completely eliminated. The time complexity is $O(n)$ to find the minimum and maximum of the array of size $n$, and the space complexity is $O(1)$ as it uses a constant amount of extra memory.
"""

class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        return max(0, max_val - min_val - 2 * k)