# Construct Binary Tree from Inorder and Postorder Traversal
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree

"""
This recursive algorithm constructs the binary tree by popping the last element from the `postorder` array to identify the current root node and using a precomputed hash map of `inorder` indices to split the tree into left and right subtrees in $O(1)$ time. Because `postorder` is processed from back to front, the algorithm recursively builds the right subtree before the left subtree using index bounds. It runs in **$O(N)$ time complexity** because each node is processed once, and consumes **$O(N)$ space complexity** to store the hash map and handle the recursion stack.
"""

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left: int, in_right: int) -> TreeNode | None:
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            idx = inorder_map[val]
            
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)