# Elimination Game
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Recursion

"""
This solution uses an iterative mathematical approach that tracks the first number (`head`), the distance between numbers (`step`), and the elimination direction (`left`) after each round. As the list is halved in each step, the algorithm runs in $O(\log n)$ time complexity and uses $O(1)$ space complexity.
"""

class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True
        remaining = n
        
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
            
        return head