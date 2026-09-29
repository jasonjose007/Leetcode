#  Check if There Is a Valid Parentheses String Path
# Platform: LeetCode
# Difficulty: Hard
# Topics: Array, Dynamic Programming, Matrix, Bracket Sequences

"""
This solution uses Depth-First Search (DFS) with memoization to explore all possible paths from the top-left to the bottom-left of the grid while tracking the running balance of parentheses (treating '(' as +1 and ')' as -1). It prunes branches early if the balance drops below zero, if the path length parity is invalid, or if a specific `(row, col, balance)` state has already been visited and failed. The time complexity is $O(m \cdot n \cdot (m + n))$ and the space complexity is $O(m \cdot n \cdot (m + n))$ to store the memoization states and recursion stack.
"""

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        max_len = m + n - 1
        if max_len % 2 != 0:
            return False
        
        memo = set()

        def dfs(r, c, balance):
            if balance < 0:
                return False
            if r == m - 1 and c == n - 1:
                return balance == 1 if grid[r][c] == ')' else False
            
            state = (r, c, balance)
            if state in memo:
                return False
            
            # Move down
            if r + 1 < m:
                next_balance = balance + (1 if grid[r+1][c] == '(' else -1)
                if dfs(r + 1, c, next_balance):
                    return True
            
            # Move right
            if c + 1 < n:
                next_balance = balance + (1 if grid[r][c+1] == '(' else -1)
                if dfs(r, c + 1, next_balance):
                    return True
            
            memo.add(state)
            return False

        init_balance = 1 if grid[0][0] == '(' else -1
        return dfs(0, 0, init_balance)