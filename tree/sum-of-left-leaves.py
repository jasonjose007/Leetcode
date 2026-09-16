# Sum of Left Leaves
# Platform: LeetCode
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

"""
This solution uses a recursive depth-first search (DFS) to traverse the binary tree, checking at each node whether its left child is a leaf node (a node with no children) to add its value to the running sum. If the left child is not a leaf, or if a right child exists, the algorithm recursively explores those subtrees to find other left leaves. The time complexity is $O(N)$ because it visits every node exactly once, and the space complexity is $O(H)$ (where $H$ is the tree height) due to the call stack during recursion.
"""

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        
        if root.right:
            ans += self.sumOfLeftLeaves(root.right)
            
        return ans