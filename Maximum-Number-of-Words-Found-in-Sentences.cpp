1class Solution {
2public:
3    int mostWordsFound(vector<string>& sentences) {
4        int maxWords = 0;
5
6        for(string s : sentences) {
7            int words = 1;
8            for(char c : s) {
9                if(c == ' ')
10                    words++;
11            }
12
13            maxWords = max(maxWords, words);
14        }
15
16        return maxWords;
17    }
18};