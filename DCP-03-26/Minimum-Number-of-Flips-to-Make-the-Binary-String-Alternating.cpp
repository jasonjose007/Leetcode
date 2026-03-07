1class Solution {
2public:
3    int minFlips(string s) {
4        int n = s.size();
5        string t = s + s;
6
7        string alt1 = "", alt2 = "";
8
9        for(int i = 0; i < 2*n; i++){
10            alt1 += (i % 2 ? '1' : '0');
11            alt2 += (i % 2 ? '0' : '1');
12        }
13
14        int diff1 = 0, diff2 = 0;
15        int res = INT_MAX;
16
17        int l = 0;
18
19        for(int r = 0; r < 2*n; r++){
20            if(t[r] != alt1[r]) diff1++;
21            if(t[r] != alt2[r]) diff2++;
22
23            if(r - l + 1 > n){
24                if(t[l] != alt1[l]) diff1--;
25                if(t[l] != alt2[l]) diff2--;
26                l++;
27            }
28
29            if(r - l + 1 == n)
30                res = min(res, min(diff1, diff2));
31        }
32
33        return res;
34    }
35};