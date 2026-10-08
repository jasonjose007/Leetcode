# Univalued Binary Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

"""
This solution uses a Depth-First Search (DFS) approach to recursively traverse the binary tree, checking whether every node shares the exact same value as the root. If it encounters any node with a differing value, it immediately returns `false`; otherwise, it returns `true` only if all subtrees match. The time complexity is $O(N)$ and the space complexity is $O(H)$, where $N$ is the number of nodes and $H$ is the height of the tree due to the recursive call stack.
"""

class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        val = root.val
        
        def dfs(node: TreeNode | None) -> bool:
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left) and dfs(node.right)
            
        return dfs(root)