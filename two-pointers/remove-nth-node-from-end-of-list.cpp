class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;

        // Move fast n+1 steps ahead
        for (int i = 0; i <= n; i++) fast = fast->next;

        // Move both until fast hits end
        while (fast) {
            fast = fast->next;
            slow = slow->next;
        }

        // slow is just before the node to delete
        ListNode* del = slow->next;
        slow->next = slow->next->next;
        delete del;

        return dummy.next;
    }
};