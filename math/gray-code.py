# Gray Code
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Backtracking, Bit Manipulation

"""
This solution generates the Gray code sequence by applying the standard mathematical formula $G_i = i \oplus \lfloor i/2 \rfloor$ to every integer from $0$ to $2^n - 1$ using a single-line list comprehension and bitwise operations. The time complexity is $O(2^n)$ because it computes a result for each of the $2^n$ possible values, and the space complexity is also $O(2^n)$ to store and return the resulting list of numbers.
"""

class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]