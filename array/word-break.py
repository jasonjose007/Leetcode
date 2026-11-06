# Word Break
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, String, Dynamic Programming, Trie, Memoization, Brute-Force Search

"""
This solution uses a bottom-up dynamic programming approach, where `dp[i]` indicates whether the prefix `s[:i]` can be segmented into words from the dictionary. It iterates through all possible lengths `i` of the string and checks every possible split point `j`; if the prefix `s[:j]` is valid (`dp[j] == True`) and the remaining substring `s[j:i]` exists in the `word_set`, then `dp[i]` is marked as true. The time complexity is $O(n^2 \cdot m)$—where $n$ is the length of the string and $m$ is the maximum word length (due to substring slicing and set lookups)—and the space complexity is $O(n + m)$ to store the DP array and the hash set.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]