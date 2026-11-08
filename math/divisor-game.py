# Divisor Game
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Dynamic Programming, Brainteaser, Game Theory, Impartial Game

"""
This solution uses a game theory approach based on mathematical induction, determining that the starting player wins if and only if $N$ is even. If $N$ is even, the first player can always choose $1$ to leave an odd number for the opponent, eventually forcing a win; if $N$ is odd, any chosen divisor will result in an even number for the opponent, leading to a loss. Because it only requires a single modulo operation, the time complexity is $O(1)$ and the space complexity is $O(1)$.
"""

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0