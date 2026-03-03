1class Solution {
2public:
3    vector<int> helper(string s, int n) {
4        int len = 0;
5        int i = 1;
6        vector<int> lps(n, 0);
7
8        lps[0] = 0;
9        while(i < n) {
10            if(s[i] == s[len]) {
11                len++;
12                lps[i] = len;
13                i++;
14            }
15            else {
16                if(len != 0) {
17                    len = lps[len - 1];
18                }
19                else {
20                    lps[i] = 0;
21                    i++;
22                }
23            }
24        }
25        return lps;
26    }
27
28    bool repeatedSubstringPattern(string s) {
29        int n = s.length();
30        vector<int> lps = helper(s, n);
31
32        int ans = lps[n-1];
33
34        if (ans > 0 && n % (n - ans) == 0) {
35            return true;
36        }
37        return false;
38    }
39};