class Solution {
public:
    string getHint(string secret, string guess) {
        map<char,int> s,g;
    for(char ch:secret){
        s[ch]++;
    }
    for(char ch:guess){
        g[ch]++;
    }
    int c=0;
    string a="0123456789";
    for(char i:a){
        if(s.find(i)!=s.end()&&g.find(i)!=g.end()) c+=min(s[i],g[i]);
    }
    int b=0;
    for(int i=0;secret[i];i++){
        if(secret[i]==guess[i]) b++;
    }
    return to_string(b)+"A"+to_string(c-b)+"B";
    }
};