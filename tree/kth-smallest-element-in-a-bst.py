# Kth Smallest Element in a BST
# Platform: LeetCode
# Difficulty: Medium
# Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree

"""
This algorithm performs an **iterative in-order traversal** using an explicit stack to visit the Binary Search Tree's nodes in sorted (ascending) order, stopping early as soon as the $k$-th node is popped. 

The **time complexity** is $O(H + k)$, where $H$ is the tree height, because it only traverses to the leftmost leaf and visits the first $k$ nodes (worst-case $O(N)$). The **space complexity** is $O(H)$ to hold the stack of ancestor nodes, which is $O(\log N)$ for a balanced tree and $O(N)$ for a skewed tree.
"""

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1