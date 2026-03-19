1class Solution:
2    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        curr=head
4        while curr and curr.next:
5            if curr.val==curr.next.val:
6                curr.next=curr.next.next
7            else:
8                curr=curr.next
9        return head
10     
11