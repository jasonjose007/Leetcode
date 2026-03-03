1class Solution {
2public:
3    int scoreOfString(string s) {
4        int score=0;
5        for(int i=1;s[i];i++)
6        score+=abs(s[i]-s[i-1]);
7        return score;
8    }
9};