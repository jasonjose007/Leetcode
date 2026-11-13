# Combinations
# Platform: LeetCode
# Difficulty: Medium
# Topics: Backtracking

"""
This solution uses a **backtracking** algorithm with **pruning** to systematically build all valid combinations of length $k$ from numbers 1 to $n$. The loop optimizes performance by stopping early (`n - needed + 2`) when remaining numbers are insufficient to complete a size-$k$ combination. The time complexity is $O(\binom{n}{k} \cdot k)$ to generate and copy all valid combinations, and the space complexity is $O(k)$ for the recursion stack and current path storage (excluding the output list).
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, current: list[int]):
            if len(current) == k:
                result.append(current.copy())
                return
            
            needed = k - len(current)
            for i in range(start, n - needed + 2):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(1, [])
        return result