# Word Search
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, String, Backtracking, Depth-First Search, Matrix

"""
This solution uses **Depth-First Search (DFS) with backtracking**, preceded by early-exit optimizations that check character frequencies and reverse the word if the starting letter is rarer than the ending letter to speed up the search. The algorithm temporarily modifies the board in place to mark visited cells during recursion, then restores them. The **time complexity** is $O(N \cdot M \cdot 4^L)$ in the worst case, where $N \times M$ is the board size and $L$ is the word length, while the **space complexity** is $O(L)$ to store the recursion stack.
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        from collections import Counter
        
        board_count = Counter(r for row in board for r in row)
        word_count = Counter(word)
        for char, count in word_count.items():
            if board_count[char] < count:
                return False
                
        if word_count[word[0]] > word_count[word[-1]]:
            word = word[::-1]
            
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
                
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
                     
            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False