# Lowest Common Ancestor of a Binary Search Tree
# Platform: LeetCode
# Difficulty: Medium
# Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor

"""
This solution uses an iterative approach that takes advantage of the Binary Search Tree (BST) property where left children are smaller and right children are larger than the current node. It starts at the root and traverses downward, moving left if both target values are smaller than the current node, right if both are larger, and stopping when they diverge (or one equals the current node), which identifies the Lowest Common Ancestor. The time complexity is $O(h)$—where $h$ is the height of the tree—and the space complexity is $O(1)$ because it uses only a few pointers for iteration without recursion.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr