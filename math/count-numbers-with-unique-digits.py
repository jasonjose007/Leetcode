# Count Numbers with Unique Digits
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Dynamic Programming, Backtracking

"""
This solution uses a combinatorics approach to calculate the number of unique-digit numbers for each length from $2$ to $n$. For a number of length $i$, the first digit has $9$ choices (1–9), the second has $9$ choices (
0–9 excluding the first), the third has $8$, and so on, which is accumulated into a running total. The time complexity is $O(n)$ because it iterates from $2$ to $n$, and the space complexity is $O(1)$ as it only uses a few variables for tracking the counts.
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        count = 10
        unique_digits = 9
        available_digits = 9
        
        for i in range(2, n + 1):
            unique_digits *= available_digits
            count += unique_digits
            available_digits -= 1
            
        return count