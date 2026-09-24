# Smallest Index With Digit Sum Equal to Index
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math

"""
This solution uses a linear scan to iterate through the array, using `enumerate` to track both the index and the value of each element. For each number, it converts the integer to a string to sum its individual digits and checks if this sum equals the current index, returning the first index that satisfies the condition or `-1` if none is found. The time complexity is $O(N \cdot M)$, where $N$ is the number of elements and $M$ is the average number of digits per integer, and the space complexity is $O(M)$ to store the string representation of each number.
"""

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = sum(int(c) for c in str(num))
            if digit_sum == i:
                return i
        return -1