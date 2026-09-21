# Add to Array-Form of Integer
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math

"""
This solution simulates manual addition from right to left by iterating backward through the `num` array while adding any remaining value of `k` as a `carry`. In each iteration, it extracts the last digit of the current sum using modulo-10, updates the carry using integer division, and finally reverses the result list since digits were appended in reverse order. The time complexity is $O(\max(N, \log_{10} K))$, where $N$ is the length of `num`, and the space complexity is $O(\max(N, \log_{10} K))$ to store the result.
"""

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1
        res = []
        carry = k
        
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            res.append(carry % 10)
            carry //= 10
            
        return res[::-1]