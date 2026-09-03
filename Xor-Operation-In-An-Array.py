# XOR Operation in an Array
# Difficulty: Easy
# Topics: Math, Bit Manipulation

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_sum(x: int) -> int:
            if x < 0:
                return 0
            rem = x % 4
            if rem == 0:
                return x
            if rem == 1:
                return 1
            if rem == 2:
                return x + 1
            return 0

        s = start // 2
        y = xor_sum(s + n - 1) ^ xor_sum(s - 1)
        lsb = (start & 1) & (n & 1)
        return (y << 1) | lsb