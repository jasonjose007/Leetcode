# Maximize Sum of Squares of Digits
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Greedy

"""
This Python solution uses a greedy algorithm to construct the largest possible number digit by digit from left to right. In each of the `num` positions, it assigns the maximum possible digit (up to 9) while ensuring that the remaining `rem_num` positions can still satisfy the leftover `sum` using at most 9 per position. The time complexity is $O(\text{num})$ and the space complexity is $O(\text{num})$ to store the result string.
"""

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        
        res = []
        for i in range(num):
            rem_num = num - 1 - i
            d = min(9, sum - rem_num)
            res.append(str(d))
            sum -= d
            
        return "".join(res)