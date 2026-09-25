# Flatten Binary Tree to Linked List
# Platform: LeetCode
# Difficulty: Medium
# Topics: Linked List, Stack, Tree, Depth-First Search, Binary Tree

"""
This solution uses Morris Traversal to flatten the binary tree in-place by iteratively finding the rightmost node of the current node's left subtree and attaching the current node's right subtree to it. The left subtree is then moved to the right child pointer, and the left pointer is set to null before moving to the next node. The time complexity is $O(N)$ because every node is visited a constant number of times, and the space complexity is $O(1)$ since it modifies the tree in-place without using any extra memory for recursion or a stack.
"""

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right