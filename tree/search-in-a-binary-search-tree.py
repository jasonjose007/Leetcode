# Search in a Binary Search Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Binary Search Tree, Binary Tree

"""
This solution uses an iterative search that leverages the Binary Search Tree property, comparing the target value to the current node and moving to the left child if it is smaller or the right child if it is larger until the value is found or the tree is exhausted. The time complexity is $O(H)$, where $H$ is the tree height—averaging $O(\log N)$ for a balanced tree and degrading to $O(N)$ in the worst-case for a skewed tree. Because it uses a single pointer inside a loop rather than recursion, it achieves an optimal $O(1)$ auxiliary space complexity.
"""

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        curr = root
        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr