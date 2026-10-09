# Edit Distance
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Dynamic Programming

"""
This solution implements a space-optimized dynamic programming approach (Wagner–Fischer algorithm) to compute the Levenshtein distance by iteratively evaluating the minimum cost among insertion, deletion, and substitution. Instead of a full 2D grid, it maintains a
 single 1D array sized to the shorter string and uses a `prev` variable to store the top-left diagonal value during in-place updates. Consequently, the algorithm runs in **$O(m \times n)$ time** and **$O(\min(m, n))$ space**, where $m$ and $n$ are the lengths of the two words.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
        
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                prev = temp
                
        return dp[n]