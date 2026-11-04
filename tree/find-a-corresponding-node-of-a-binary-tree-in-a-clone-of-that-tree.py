# Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

"""
This solution uses a recursive **depth-first search (DFS)** to simultaneously traverse both the original and cloned binary trees. It checks if the current node in the original tree is the target; if so, it immediately returns the corresponding node in the cloned tree. The time complexity is **$O(N)$** and the space complexity is **$O(H)$** (where $N$ is the number of nodes and $H$ is the tree's height for the call stack).
"""

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None or original == target:
            return cloned
        
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        
        return self.getTargetCopy(original.right, cloned.right, target)