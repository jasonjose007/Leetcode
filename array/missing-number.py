# Missing Number
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

"""
This solution uses the mathematical Gauss summation formula to find the expected sum of integers from $0$ to $n$, where $n$ is the length of the array. It then subtracts the actual sum of the elements in `nums` from this expected sum to reveal the missing number. The algorithm runs in $O(n)$ time due to summing the array and $O(1)$ auxiliary space since it only uses a few variables.
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum