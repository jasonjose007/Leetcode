# Lowest Common Ancestor of a Binary Tree
# Platform: LeetCode
# Difficulty: Medium
# Topics: Tree, Depth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor

"""
This solution uses a recursive Depth-First Search (DFS) post-order traversal to search for nodes `p` and `q` from the bottom up. If the current root is `null`, `p`, or `q`, it returns the root; otherwise, it checks both subtrees, returning the current root if `p` and `q` are found in separate branches, or bubbling up the non-null result if they are in the same branch. The time complexity is $O(N)$ and the space complexity is $O(H)$, where $N$ is the number of nodes and $H$ is the height of the tree due to the recursive call stack.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right