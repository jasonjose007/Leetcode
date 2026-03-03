1class Solution {
2public:
3    string longestCommonPrefix(vector<string>& strs) {
4        if (strs.empty()) return "";
5        string prefix = strs[0];
6        for (int i = 0; i < (int)strs.size(); i++) {
7            int j = 0;
8            while(j < (int)prefix.size() && j < (int)strs[i].size() &&
9                prefix[j] == strs[i][j]) {
10                    j++;
11                }
12                prefix = prefix.substr(0,j);
13                if (prefix.empty()) return "";
14
15
16        }
17        return prefix;
18    }
19};