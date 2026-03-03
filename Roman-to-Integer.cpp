1class Solution {
2    public int romanToInt(String s) {
3        int ans = 0, num = 0;
4        for (int i = s.length() - 1; i >= 0; i--) {
5            switch (s.charAt(i)) {
6                case 'I':
7                    num = 1;
8                    break;
9                case 'V':
10                    num = 5;
11                    break;
12                case 'X':
13                    num = 10;
14                    break;
15                case 'L':
16                    num = 50;
17                    break;
18                case 'C':
19                    num = 100;
20                    break;
21                case 'D':
22                    num = 500;
23                    break;
24                case 'M':
25                    num = 1000;
26                    break;
27            }
28            if (4 * num < ans)
29                ans -= num;
30            else
31                ans += num;
32        }
33        return ans;
34
35    }
36}