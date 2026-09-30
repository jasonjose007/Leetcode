# Maximum Nesting Depth of Two Valid Parentheses Strings
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack, Bracket Sequences

"""
This algorithm iterates through the parenthesis string while tracking the current nesting depth, alternating the assignment of each parenthesis between two groups based on the parity of its depth (`depth % 2`). This ensures that the maximum nesting depth within each resulting group is minimized, as consecutive opening parentheses are split evenly. The time complexity is $O(N)$ and the space complexity is $O(N)$ to store the result array, where $N$ is the length of the string.
"""

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        for char in seq:
            if char == '(':
                depth += 1
                res.append(depth % 2)
            else:
                res.append(depth % 2)
                depth -= 1
        return res