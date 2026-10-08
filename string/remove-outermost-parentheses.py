# Remove Outermost Parentheses
# Platform: LeetCode
# Difficulty: Easy
# Topics: String, Stack, Bracket Sequences

"""
This solution uses a tracking variable `depth` to iterate through the string and identify the primitive decomposition of valid parentheses. It appends a parenthesis to the result list only if its depth is strictly greater than zero, effectively stripping away the outermost matching pair of each primitive group. Both the time and space complexities are $O(n)$, where $n$ is the length of the string, because it visits each character once and stores the result in a list proportional to the input size.
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(char)
        return "".join(res)