# Bulb Switcher
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Brainteaser

"""
A bulb at position $k$ remains on only if it is toggled an odd number of times, which happens exclusively for perfect squares because their factors pair up except for the square root itself. Consequently, the problem reduces to counting the number of perfect squares less than or equal to $n$, which is directly calculated using the integer square root $\lfloor\sqrt{n}\rfloor$. This mathematical approach achieves $O(1)$ time complexity and $O(1)$ auxiliary space complexity.
"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        import math
        return math.isqrt(n)