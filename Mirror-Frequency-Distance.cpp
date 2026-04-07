1class Solution {
2public:
3    int mirrorFrequency(string s) {
4        unordered_map<char, int> mp;
5        int sum = 0;
6        for (char ch : s)
7            mp[ch]++;
8        for (char ch : s) {
9            char mir;
10            if (isalpha(ch))
11                mir = (char)('z' - (ch - 'a'));
12            else
13                mir = (char)('9' - (ch - '0'));
14            if (mp.find(mir) != mp.end()) {
15                sum += abs(mp[ch] - mp[mir]);
16                mp[ch] = 0;
17                mp[mir] = 0;
18            } else {
19                sum += mp[ch];
20                mp[ch] = 0;
21            }
22        }
23        return sum;
24    }
25};