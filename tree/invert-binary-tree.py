# Invert Binary Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

"""
This solution uses a recursive Depth-First Search (DFS) algorithm to invert the binary tree by traversing to the bottom and swapping each node's left and right children. By simultaneously making recursive calls on `root.right` and `root.left`, the left and right subtrees are inverted and assigned to opposite sides as the call stack unwinds. The algorithm runs in **$O(N)$ time complexity** because every node is visited once, and **$O(H)$ space complexity** (where $H$ is the tree height, up to $O(N)$ in the worst case) to store the call stack.
"""

class Solution:

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.left, root.right = self.invertTree(
            root.right
        ), self.invertTree(root.left)
        return root