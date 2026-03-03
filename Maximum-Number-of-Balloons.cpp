1class Solution {
2public:
3    int maxNumberOfBalloons(string text) {
4         std::map<char, int> etalon{
5            {'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}};
6
7        std::map<char, int> temp {
8            {'b', 0}, {'a', 0}, {'l', 0}, {'o', 0}, {'n', 0}};
9        
10        for (int i = 0; i < text.size(); i++){
11            temp[text[i]] = temp[text[i]] + 1;
12        }
13        
14        int count = 0;
15        char* balon = "balon";
16        while(true) {
17            for (int i = 0; i < 5; i++) {
18                temp[balon[i]] -= etalon[balon[i]];
19                if (temp[balon[i]] < 0)
20                    return count;
21            }
22            count++;
23        }
24    }
25};