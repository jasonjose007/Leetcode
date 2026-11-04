# Binary Tree Level Order Traversal II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Tree, Breadth-First Search, Binary Tree

"""
This solution uses a Breadth-First Search (BFS) approach with a queue to traverse the binary tree level by level, collecting the values of each level into a list. It then reverses the final list of level values before returning it, ensuring the output starts from the bottom level and goes up to the root. The time complexity is $O(N)$ and the space complexity is $O(N)$ (where $N$ is the number of nodes), as every node is visited once and stored in memory.
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_values = []
            next_queue = []
            for node in queue:
                level_values.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(level_values)
            queue = next_queue
            
        return result[::-1]