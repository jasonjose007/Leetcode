class Solution {
public:
    string sortSentence(string s) {
    vector<string>ans(9,"0");
        for(int i=0;s[i];i++){
            if(s[i]==' ') continue;
            string word="";
            while(s[i]<'0' || s[i]>'9'){
                word+=s[i];
                i++;
            }
            
            int index=s[i]-'0';
            ans[index-1]=word;
        }
        string sen="";
        for(auto val:ans){
            if(val=="0") break;
            sen+=val;
            sen+=' ';

        }
        return sen.substr(0,sen.size()-1);
    }

};