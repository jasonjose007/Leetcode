# Stone Game IV
# Difficulty: Hard
# Topics: Math, Dynamic Programming, Minimax, Game Theory, Nim Game, Sprague–Grundy Theorem, Zero-Sum Game

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(n + 1):
            if not dp[i]:
                k = 1
                while i + k * k <= n:
                    dp[i + k * k] = True
                    k += 1
        return dp[n]