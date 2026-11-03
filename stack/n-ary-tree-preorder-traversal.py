# N-ary Tree Preorder Traversal
# Platform: LeetCode
# Difficulty: Easy
# Topics: Stack, Tree, Depth-First Search

"""
This solution uses an iterative depth-first search (DFS) algorithm with a stack to traverse the N-ary tree in preorder (root, followed by children from left to right). By popping nodes from the stack and pushing their children in reverse order, it ensures that the leftmost child is processed next. The time complexity is $O(N)$ and the space complexity is $O(H)$, where $N$ is the number of nodes and $H$ is the height of the tree.
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                for child in reversed(node.children):
                    if child:
                        stack.append(child)
                        
        return result