1class Solution {
2public:
3    bool isPalindrome(int x) {
4        if (x<0 || (x%10 == 0 && x!=0)) return false;
5        long long rev = 0;
6        while (x>rev) {
7            rev = (rev*10) + (x%10);
8            x/=10;
9        }
10        return (rev == x || x == rev/10);
11    }
12};