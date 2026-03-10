1class Solution {
2public:
3    int maximum69Number (int num) {
4        string s=to_string(num);
5        for(int i=0;s[i];i++){
6            if(s[i]=='6'){
7                s[i]='9';
8                break;
9            }
10        }
11        return stoi(s);
12    }
13};