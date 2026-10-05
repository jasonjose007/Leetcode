# Score of Parentheses
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack, Bracket Sequences

"""
This solution uses a depth-tracking approach to calculate the score without needing an explicit stack. As it iterates through the string, it increments the `depth` for every opening parenthesis `(` and decrements it for every closing parenthesis `)`. When it encounters the end of the base pair `()` (i.e., `s[i-1] == '('`), it adds $2^{\text{depth}}$ to the total score, reflecting the doubling effect of nested parentheses. The algorithm runs in $O(n)$ time complexity and $O(1)$ space complexity.
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        depth = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    ans += 1 << depth
        return ans