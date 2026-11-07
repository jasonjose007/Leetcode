# Nim Game
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Brainteaser, Minimax, Game Theory, Nim Game, Impartial Game

"""
The algorithm determines the outcome of the Nim game by using simple modulo arithmetic, recognizing that the first player can always force a win unless the starting number of stones is a multiple of 4. Since it only performs a single modulo and comparison operation, the time complexity is $O(1)$ and the space complexity is $O(1)$.
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0