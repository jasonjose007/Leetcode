# Best Time to Buy and Sell Stock II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Greedy

"""
This solution uses a **greedy approach** that iterates through the price array and captures every single upward price movement. Whenever the price on day `i` is higher than the previous day, it immediately adds that daily profit to the total `max_profit`. The algorithm runs in **$O(n)$ time complexity** (where $n$ is the number of days) and requires **$O(1)$ space complexity** since it only uses a single variable to track the running profit.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit