# Valid Sudoku
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Matrix

"""
The algorithm iterates through each cell of the board and uses a single hash set to track seen numbers across their respective rows, columns, and 3x3 sub-boxes using unique tuple keys. If any generated key is already present in the set, a duplicate rule is violated and the board is immediately deemed invalid. Because the board is fixed at 9x9 cells, both the time complexity and space complexity are **O(1)** (constant).
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != '.':
                    row_key = (i, number)
                    col_key = (number, j)
                    box_key = (i // 3, j // 3, number)
                    
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
                    
        return True