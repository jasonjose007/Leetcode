# Valid Perfect Square
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Binary Search

"""
This solution uses the **binary search** algorithm to find if a number is a perfect square by repeatedly halving the search space between `1` and `num`. It compares the square of the middle value (`mid * mid`) with the target `num`, adjusting the `left` or `right` pointers accordingly until a match is found or the pointers cross. The time complexity is **$O(\log \text{num})$** because the search range is halved in each iteration, and the space complexity is **$O(1)$** as it only uses a constant amount of extra memory.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False