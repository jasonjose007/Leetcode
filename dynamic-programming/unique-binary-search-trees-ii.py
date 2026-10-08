# Unique Binary Search Trees II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree

"""
This solution uses a recursive divide-and-conquer approach with memoization-like subproblem generation, where every number from `start` to `end` is sequentially chosen as the root. For each chosen root, it recursively generates all possible left and right subtrees and combines every possible pair to form valid Binary Search Trees. The time and space complexity are both bounded by the $n$-th Catalan number, $O(4^n / n^{1/3})$, because the algorithm must explicitly construct and store every unique BST.
"""

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
        
        def generate(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
                        
            return all_trees
            
        return generate(1, n)