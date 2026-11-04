# Base 7
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, String

"""
This solution converts a decimal number to base 7 by repeatedly extracting the remainder of the number divided by 7 (using modulo arithmetic) and then integer-dividing the number by 7 until it reaches zero. It handles negative numbers by recording the sign, performing the conversion on the absolute value, and appending a negative sign at the end before reversing the collected digits to form the correct result. The time and space complexities are both $O(\log_7(n))$ (or $O(\log n)$), where $n$ is the absolute value of the input number, because the number of digits in base 7 is proportional to the logarithmic growth of the input.
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        is_negative = num < 0
        num = abs(num)
        
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
            
        if is_negative:
            digits.append("-")
            
        return "".join(reversed(digits))