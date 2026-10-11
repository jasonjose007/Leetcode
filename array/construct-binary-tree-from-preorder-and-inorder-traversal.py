# Construct Binary Tree from Preorder and Inorder Traversal
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree

"""
This iterative algorithm uses a stack to build the tree, continuously attaching each new preorder node as the left child of the stack's top node until that top node matches the current `inorder` element. Once a match occurs, it pops matching ancestors to backtrack to the correct parent and attaches the new node as its right child. Because each node is pushed and popped from the stack at most once, the algorithm operates in $O(N)$ time complexity and $O(N)$ auxiliary space complexity, where $N$ is the number of nodes.
"""

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0
        
        for val in preorder[1:]:
            node = TreeNode(val)
            if stack[-1].val != inorder[inorder_idx]:
                stack[-1].left = node
            else:
                while stack and stack[-1].val == inorder[inorder_idx]:
                    u = stack.pop()
                    inorder_idx += 1
                u.right = node
            stack.append(node)
            
        return root