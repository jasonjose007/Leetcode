1class Solution {
2public:
3    int minOperations(string s) {
4        int p1 = 0;
5        int p2 = 0;
6        
7        for(int i = 0; i < s.length(); i++) {
8            if(i % 2 == 0) {
9                if(s[i] != '0') p1++;
10                if(s[i] != '1') p2++;
11            }
12            else {
13                if(s[i] != '1') p1++;
14                if(s[i] != '0') p2++;
15            }
16        }
17        
18        return min(p1, p2);
19    }
20};