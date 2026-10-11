# Sum of Squares of Special Elements 
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Enumeration

"""
The algorithm iterates through all 1-based indices $i$ from $1$ to $n$, identifying "special" indices where $n$ is divisible by $i$ (`n % i == 0`). For each valid index, it computes the square of the corresponding element `nums[i - 1]` and accumulates them into a final sum. This approach runs in **$O(n)$ time** by inspecting each index once and uses **$O(1)$ auxiliary space** by calculating the sum on the fly via a generator expression.
"""

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(nums[i - 1] * nums[i - 1] for i in range(1, n + 1) if n % i == 0)