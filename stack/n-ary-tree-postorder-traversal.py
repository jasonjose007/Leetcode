# N-ary Tree Postorder Traversal
# Platform: LeetCode
# Difficulty: Easy
# Topics: Stack, Tree, Depth-First Search

"""
This solution uses an iterative approach with a stack to traverse the N-ary tree in a modified preorder sequence (root, right-to-left children), which is then reversed to achieve the correct postorder traversal (left-to-right children, root). By popping nodes from the stack, appending their values, and pushing their children onto the stack from left to right, it visits every node efficiently. The time complexity is $O(N)$ and the space complexity is $O(N)$ (where $N$ is the number of nodes), as every node is processed once and stored in the stack and output list.
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.children:
                for child in node.children:
                    if child:
                        stack.append(child)
                        
        return output[::-1]