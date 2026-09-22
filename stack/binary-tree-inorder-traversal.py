# Binary Tree Inorder Traversal
# Platform: LeetCode
# Difficulty: Easy
# Topics: Stack, Tree, Depth-First Search, Binary Tree

"""
This algorithm implements an iterative inorder traversal (left-root-right) using an explicit stack to simulate recursion. It continuously pushes nodes onto the stack while traversing to the leftmost child, then pops each node to record its value before transitioning to its right subtree. The time complexity is $O(n)$ as every node is visited a constant number of times, and the space complexity is $O(h)$ (where $h$ is the tree height, up to $O(n)$ in the worst case) to store nodes in the stack.
"""

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res