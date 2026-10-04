# Convert a Number to Hexadecimal
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, String, Bit Manipulation

"""
This algorithm converts a number to hexadecimal by first applying a bitwise AND mask to handle negative integers as 32-bit two's complement numbers. It then repeatedly extracts the last 4 bits of the number using bitwise operations, maps them to the corresponding hexadecimal character, and shifts the number right until it becomes zero. Both the time and space complexities are $O(1)$ because a 32-bit integer requires at most 8 hexadecimal characters to represent.
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        num &= 0xFFFFFFFF
        hex_chars = "0123456789abcdef"
        res = []
        
        while num > 0:
            res.append(hex_chars[num & 0xF])
            num >>= 4
            
        return "".join(reversed(res))