# Maximum Alternating Sum of Squares
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Greedy, Sorting

"""
This solution uses a greedy approach by squaring each element and sorting the results in ascending order. To maximize the alternating sum, it splits the sorted squares at the midpoint, adding the larger half and subtracting the smaller half. The time complexity is $O(n \log n)$ due to sorting, and the space complexity is $O(n)$ to store the squared values, where $n$ is the length of `nums`.
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        m = len(sq) // 2
        return sum(sq[m:]) - sum(sq[:m])