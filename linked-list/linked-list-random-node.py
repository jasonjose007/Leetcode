# Linked List Random Node
# Platform: LeetCode
# Difficulty: Medium
# Topics: Linked List, Math, Reservoir Sampling, Randomized

class Solution:

    def __init__(self, head: ListNode | None):
        self.vals = []
        curr = head
        while curr:
            self.vals.append(curr.val)
            curr = curr.next

    def getRandom(self) -> int:
        return random.choice(self.vals)