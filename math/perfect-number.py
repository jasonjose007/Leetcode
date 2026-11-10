# Perfect Number
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math

"""
This algorithm determines if a number is perfect by iterating from 2 up to the square root of `num` to find all of its proper divisors, adding both the divisor and its counterpart (`num // i`) to a running sum. It then checks if this sum equals the original `num`. The time complexity is $O(\sqrt{n})$ and the space complexity is $O(1)$.
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i * i != num:
                    total += num // i
            i += 1
            
        return total == num