# Intersection of Two Linked Lists
# Platform: LeetCode
# Difficulty: Easy
# Topics: Hash Table, Linked List, Two Pointers

"""
This solution uses a two-pointer approach that traverses both linked lists simultaneously. When a pointer reaches the end of its list, it is redirected to the head of the other list, effectively equalizing their lengths so that they meet at the intersection node (or at `None` if no intersection exists). The time complexity is $O(N + M)$ where $N$ and $M$ are the lengths of the two lists, and the space complexity is $O(1)$ as it only uses two pointers.
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        ptrA = headA
        ptrB = headB
        
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
            
        return ptrA