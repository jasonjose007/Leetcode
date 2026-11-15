# Number of Sub-arrays With Odd Sum
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Dynamic Programming, Prefix Sum

"""
This algorithm tracks the parity of the running prefix sum using a bitwise flag (`curr`) while counting how many even and odd prefix sums have been seen so far (starting with `even = 1` for an empty prefix of sum 0). At each element, a subarray ending there has an odd sum whenever the current prefix sum is paired with an earlier prefix sum of the opposite parity, so the solution adds that opposite count to `ans` and increments the current parity's counter. This single-pass approach runs in $O(n)$ time, where $n$ is the length of `arr`, and uses $O(1)$ extra space.
"""

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1
        odd = 0
        curr = 0
        ans = 0
        for x in arr:
            curr ^= x & 1
            if curr:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % MOD