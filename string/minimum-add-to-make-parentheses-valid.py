# Minimum Add to Make Parentheses Valid
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack, Greedy, Bracket Sequences

"""
This solution iterates through the string while maintaining a `balance` of unmatched open parentheses and tracking `open_needed` for unmatched closing parentheses. When a closing bracket appears, it either cancels out an existing open bracket or increments `open_needed`, and the final answer is simply the sum of `open_needed` and the remaining `balance`. The algorithm runs in **$O(n)$ time** and uses **$O(1)$ space**, where $n$ is the length of the string.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    open_needed += 1

        return open_needed + balance