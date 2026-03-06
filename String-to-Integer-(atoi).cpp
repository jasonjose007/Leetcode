1class Solution {
2public:
3    int myAtoi(string s) {
4        int i = 0, sign = 1;
5        long num = 0;
6
7        while (i < s.size() && s[i] == ' ') i++;
8        if (s[i] == '+' || s[i] == '-') sign = (s[i++] == '-') ? -1 : 1;
9
10        while (i < s.size() && isdigit(s[i])) {
11            num = num * 10 + (s[i++] - '0');
12            if (num * sign > INT_MAX) return INT_MAX;
13            if (num * sign < INT_MIN) return INT_MIN;
14        }
15        return num * sign;
16    }
17};