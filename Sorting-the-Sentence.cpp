1class Solution {
2public:
3    string sortSentence(string s) {
4    vector<string>ans(9,"0");
5        for(int i=0;s[i];i++){
6            if(s[i]==' ') continue;
7            string word="";
8            while(s[i]<'0' || s[i]>'9'){
9                word+=s[i];
10                i++;
11            }
12            
13            int index=s[i]-'0';
14            ans[index-1]=word;
15        }
16        string sen="";
17        for(auto val:ans){
18            if(val=="0") break;
19            sen+=val;
20            sen+=' ';
21
22        }
23        return sen.substr(0,sen.size()-1);
24    }
25
26};