1class Solution {
2public:
3    int reverseDegree(string s) {
4     int sum=0;
5     for(int i=0;s[i];i++){
6     int val=(s[i]-'a');
7     sum+=(i+1)*abs(26-val);}
8    return sum;
9    }
10};