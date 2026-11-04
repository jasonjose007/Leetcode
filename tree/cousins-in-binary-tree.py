# Cousins in Binary Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

"""
This solution uses a Depth-First Search (DFS) traversal to record the depth and parent of nodes `x` and `y` in a hash map. It then compares this stored information to determine if both nodes share the same depth while having different parents. The algorithm operates in $O(N)$ time complexity and $O(N)$ space complexity, where $N$ is the number of nodes in the binary tree.
"""

class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        info = {}
        
        def dfs(node, depth, parent):
            if not node:
                return
            if node.val == x or node.val == y:
                info[node.val] = (depth, parent)
            dfs(node.left, depth + 1, node)
            dfs(node.right, depth + 1, node)
            
        dfs(root, 0, None)
        
        depth_x, parent_x = info[x]
        depth_y, parent_y = info[y]
        
        return depth_x == depth_y and parent_x != parent_y