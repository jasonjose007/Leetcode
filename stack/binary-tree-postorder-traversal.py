# Binary Tree Postorder Traversal
# Platform: LeetCode
# Difficulty: Easy
# Topics: Stack, Tree, Depth-First Search, Binary Tree

"""
This solution uses an iterative approach that modifies a standard preorder traversal (Root-Left-Right) by pushing the left child onto the stack before the right child, resulting in a Root-Right-Left order. Reversing this resulting list at the end produces the correct postorder traversal (Left-Right-Root). Both the time and space complexities are $O(N)$, where $N$ is the number of nodes in the binary tree, as every node is visited once and the stack and output list store up to $N$ nodes.
"""

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return output[::-1]