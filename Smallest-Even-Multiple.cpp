1class Solution {
2public:
3    int smallestEvenMultiple(int n) {
4        if(n%2==1)
5            return n*2;
6        return n;
7    }
8};