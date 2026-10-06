# Unique Binary Search Trees
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree

"""
This solution uses a dynamic programming approach based on the Catalan number formula, where each tree's unique structures are built by systematically considering every number $1$ to $i$ as the root. It computes the number of unique BSTs for each size from $2$ to $n$ by multiplying the combinations of possible left subtrees (`dp[j - 1]`) and right subtrees (`dp[i - j]`). The time complexity is $O(n^2)$ due to the nested loops, and the space complexity is $O(n)$ to store the DP table.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]