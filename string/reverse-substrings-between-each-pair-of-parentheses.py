# Reverse Substrings Between Each Pair of Parentheses
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack, Bracket Sequences

"""
This solution uses a "wormhole" traversal algorithm that first matches every opening and closing parenthesis using a stack to record their indices. It then iterates through the string using a directional pointer that instantly teleports to the matching parenthesis and reverses its direction of movement whenever it encounters one. The time and space complexities are both $O(n)$, where $n$ is the length of the string, because it processes each character a constant number of times and stores indices and the result in structures proportional to $n$.
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        d = 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d

        return "".join(res)