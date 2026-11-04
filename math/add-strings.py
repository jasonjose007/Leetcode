# Add Strings
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, String, Simulation

"""
This algorithm simulates manual right-to-left addition (grade-school addition) by using two pointers (`i` and `j`) to iterate through both strings from their least significant digits to their most significant digits, maintaining a `carry` value along the way. The resulting digits are stored in a list and finally reversed and joined to produce the correct sum string. The time complexity is $O(\max(N, M))$ and the space complexity is $O(\max(N, M))$, where $N$ and $M$ are the lengths of the input strings.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0
            
            total = d1 + d2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            i -= 1
            j -= 1
            
        return "".join(reversed(res))