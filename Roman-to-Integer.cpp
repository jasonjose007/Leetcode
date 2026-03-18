1class Solution {
2public:
3
4    int charToNum( char a ){
5        switch (a) {
6            case 'I' : return 1 ;
7            case 'V' : return 5 ;
8            case 'X' : return 10 ;
9            case 'L' : return 50;
10            case 'C' : return 100;
11            case 'D' : return 500;
12            case 'M' : return 1000;
13            default : return 0 ;
14        }
15    }
16
17    int romanToInt(string s) {
18        int n = s.size() ;
19        int res = 0 ;
20        for ( int i =0; i < n ; i++){
21             if (i + 1 < n && charToNum(s[i]) < charToNum(s[i+1]) ){
22                res -= charToNum(s[i]) ;
23
24             }else {
25                res += charToNum(s[i]) ;
26             }
27
28        }
29        return res ;
30        
31    }
32};