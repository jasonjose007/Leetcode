# Root Equals Sum of Children
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Binary Tree

"""
This algorithm checks if the binary tree satisfies the "Root Equals Sum of Children" property by directly comparing the value of the root node to the sum of the values of its left and right children. Because it only performs a single constant-time arithmetic and comparison operation, the time complexity is $O(1)$ and the space complexity is $O(1)$.
"""

class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        return root.val == root.left.val + root.right.val