# Palindrome Linked List
# Difficulty: Easy
# Topics: Linked List, Two Pointers, Stack, Recursion

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        p1 = head
        p2 = prev
        is_pal = True
        while p2:
            if p1.val != p2.val:
                is_pal = False
                break
            p1 = p1.next
            p2 = p2.next
            
        curr = prev
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        slow.next = prev
        
        return is_pal