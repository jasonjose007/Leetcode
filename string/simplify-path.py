# Simplify Path
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack

"""
This solution uses a stack-based algorithm by splitting the input path by `'/'` and iterating through each component. It pushes valid directory names onto the stack, pops from the stack when encountering `'..'` to move up a directory, and ignores empty strings and single dots (`'.'`). The algorithm runs in **$O(N)$ time** and **$O(N)$ space**, where $N$ is the length of the path, as it iterates through the split components and stores them in the stack.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')
        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        return '/' + '/'.join(stack)