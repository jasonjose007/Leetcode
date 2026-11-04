# Verify Preorder Serialization of a Binary Tree
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack, Tree, Binary Tree

"""
This solution uses a slot-counting greedy algorithm to track the capacity for nodes in the binary tree, starting with one slot for the root. As it iterates through the comma-separated traversal, each node consumes one slot, and non-null nodes provide two new child slots, immediately returning `false` if the slot count drops below zero. The algorithm achieves an optimal **$O(N)$ time complexity** by visiting each of the $N$ nodes once and an **$O(N)$ space complexity** to store the list created by splitting the string.
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        return slots == 0