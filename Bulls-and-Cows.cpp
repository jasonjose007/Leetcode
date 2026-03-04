1class Solution {
2public:
3    string getHint(string secret, string guess) {
4        map<char,int> s,g;
5    for(char ch:secret){
6        s[ch]++;
7    }
8    for(char ch:guess){
9        g[ch]++;
10    }
11    int c=0;
12    string a="0123456789";
13    for(char i:a){
14        if(s.find(i)!=s.end()&&g.find(i)!=g.end()) c+=min(s[i],g[i]);
15    }
16    int b=0;
17    for(int i=0;secret[i];i++){
18        if(secret[i]==guess[i]) b++;
19    }
20    return to_string(b)+"A"+to_string(c-b)+"B";
21    }
22};