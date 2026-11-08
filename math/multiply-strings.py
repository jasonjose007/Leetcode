# Multiply Strings
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, String, Simulation

"""
This solution simulates manual grade-school multiplication by iterating through each digit of both strings from right to left, multiplying them, and adding the results to the correct positions in an array representing the digits of the product. It handles carries dynamically by updating adjacent positions and finally strips any leading zeros before returning the string representation. The time complexity is $O(m \times n)$ and the space complexity is $O(m + n)$, where $m$ and $n$ are the lengths of the two input strings.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + pos[p2]
                
                pos[p2] = total % 10
                pos[p1] += total // 10
                
        result = "".join(map(str, pos))
        return result.lstrip("0")