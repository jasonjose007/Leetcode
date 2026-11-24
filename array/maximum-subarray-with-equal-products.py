# Maximum Subarray With Equal Products
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math, Sliding Window, Enumeration, Number Theory

"""
The algorithm uses a brute-force approach with nested loops to evaluate every contiguous subarray `nums[i..j]` by fixing a start index `i` and extending the end index `j`. As each subarray grows, it incrementally maintains the running product (`p`), greatest common divisor (`g`), and least common multiple (`l`), updating the maximum length `ans` whenever `p == l * g`. Because it checks all pairs of indices using a fixed number of variables, the time complexity is $O(n^2)$ (assuming constant-time arithmetic, ignoring logarithmic factors from `gcd`/`lcm` and big-integer growth) and the auxiliary space complexity is $O(1)$.
"""

class Solution:

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = math.gcd(g, x)
                l = math.lcm(l, x)
                if p == l * g:
                    ans = max(ans, j - i + 1)
        return ans