# Minimum Depth of Binary Tree
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))