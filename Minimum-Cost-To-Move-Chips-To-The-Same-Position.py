# Minimum Cost to Move Chips to The Same Position
# Difficulty: Easy
# Topics: Array, Math, Greedy

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = sum(1 for x in position if x % 2 == 0)
        odds = len(position) - evens
        return min(evens, odds)