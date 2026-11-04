# Generate Parentheses
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Dynamic Programming, Backtracking, Bracket Sequences

"""
This solution uses a **backtracking** algorithm to recursively build all valid combinations of parentheses by tracking the count of open and close brackets used so far. It adds an opening parenthesis if the count is less than `n`, and a closing parenthesis only if the count of closing brackets is strictly less than the opening ones to ensure validity. The time and space complexity are both $\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$, which corresponds to the $n$-th Catalan number.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(s: str, left: int, right: int):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        backtrack("", 0, 0)
        return res