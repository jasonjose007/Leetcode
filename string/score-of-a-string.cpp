class Solution {
public:
    int scoreOfString(string s) {
        int score=0;
        for(int i=1;s[i];i++)
        score+=abs(s[i]-s[i-1]);
        return score;
    }
};