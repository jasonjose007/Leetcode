1class Solution {
2public:
3    int lengthOfLastWord(string s) {
4        int len = 0;
5        for (int i = s.length() - 1; i >= 0; i--) {
6            if (s[i] != ' ') len++;
7            else if (len != 0) break;
8        }
9        return len;
10    }
11};