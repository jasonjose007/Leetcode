1class Solution {
2public:
3    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
4       
5        if(list1 == NULL)
6            return list2;
7		
8        if(list2 == NULL)
9            return list1;
10        
11        ListNode * ptr = list1;
12        if(list1 -> val > list2 -> val)
13        {
14            ptr = list2;
15            list2 = list2 -> next;
16        }
17        else
18        {
19            list1 = list1 -> next;
20        }
21        ListNode *curr = ptr;
22        while(list1 &&  list2)
23        {
24            if(list1 -> val < list2 -> val){
25                curr->next = list1;
26                list1 = list1 -> next;
27            }
28            else{
29                curr->next = list2;
30                list2 = list2 -> next;
31            }
32            curr = curr -> next;
33                
34        }
35
36        if(!list1)
37            curr -> next = list2;
38        else
39            curr -> next = list1;
40            
41        return ptr;
42       
43    }
44};