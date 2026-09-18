# Linked List Cycle
# Platform: LeetCode
# Difficulty: Easy
# Topics: Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm

"""
This solution uses **Floyd’s Cycle-Finding Algorithm** (the "tortoise and hare" approach), utilizing two pointers that traverse the linked list at different speeds—the slow pointer moves one step at a time, while the fast pointer moves two steps. If a cycle exists, the fast pointer will eventually loop around and meet the slow pointer; otherwise, the fast pointer will reach the end of the list. The time complexity is **$O(N)$** because the pointers traverse at most $N$ nodes, and the space complexity is **$O(1)$** as it only uses two pointer variables regardless of the list size.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False