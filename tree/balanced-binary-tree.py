# Balanced Binary Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Binary Tree

"""
This solution uses a bottom-up depth-first search (DFS) recursion to simultaneously compute the height of each subtree and check for balance. If any subtree is found to be unbalanced, it immediately propagates a `-1` signal upward, avoiding redundant calculations. The time complexity is $O(n)$ because it visits each node at most once, and the space complexity is $O(h)$ (where $h$ is the tree height) to account for the recursion stack.
"""

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def check(node: TreeNode | None) -> int:
            if not node:
                return 0
            left_height = check(node.left)
            if left_height == -1:
                return -1
            right_height = check(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return check(root) != -1