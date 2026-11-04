# Increasing Order Search Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree

"""
This solution uses an in-order traversal to collect all the nodes of the Binary Search Tree into a list, which naturally sorts them in ascending order. It then iterates through the list, rewiring each node's `left` pointer to `None` and its `right` pointer to the next node in the sequence to form a right-skewed tree. The time complexity is $O(N)$ and the space complexity is $O(N)$ due to storing the nodes in a list and the recursion stack, where $N$ is the number of nodes.
"""

class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
            
        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None
            return nodes[0]
        return None