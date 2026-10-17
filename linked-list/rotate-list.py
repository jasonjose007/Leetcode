# Rotate List
# Platform: LeetCode
# Difficulty: Medium
# Topics: Linked List, Two Pointers

"""
This algorithm works by first computing the length $n$ of the linked list and connecting its tail to the head to form a circular list. It then calculates the effective shift as $k \pmod n$ and traverses $n - (k \pmod n)$ steps to locate the new tail, where it breaks the cycle to establish the new head. The solution achieves an **$O(N)$ time complexity** by traversing the list twice and an **$O(1)$ auxiliary space complexity** by modifying the list pointers in place.
"""

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
            
        k %= n
        if k == 0:
            return head
            
        tail.next = head
        steps_to_new_tail = n - k
        new_tail = tail
        while steps_to_new_tail > 0:
            new_tail = new_tail.next
            steps_to_new_tail -= 1
            
        new_head = new_tail.next
        new_tail.next = None
        return new_head