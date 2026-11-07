# Swap Nodes in Pairs
# Platform: LeetCode
# Difficulty: Medium
# Topics: Linked List, Recursion

"""
This solution uses an iterative pointer-manipulation algorithm with a dummy node to swap adjacent nodes in-place. During each iteration of the `while` loop, the pointers for the first and second nodes of the current pair are carefully reassigned to reverse their order, and the pointer `curr` is advanced by two nodes to process the next pair. The algorithm operates in $O(n)$ time complexity by traversing the linked list once and $O(1)$ auxiliary space complexity because it only uses a constant number of pointers for the swaps.
"""

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            
            first.next = second.next
            second.next = first
            curr.next = second
            
            curr = first
            
        return dummy.next