# Calculate Money in Leetcode Bank
# Difficulty: Easy
# Topics: Math

class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        d = n % 7
        
        full_weeks_sum = 28 * w + 7 * (w - 1) * w // 2
        remaining_days_sum = d * w + d * (d + 1) // 2
        
        return full_weeks_sum + remaining_days_sum