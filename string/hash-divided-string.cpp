class Solution {
public:
    string stringHash(string s, int k) {
        string ans="";
        int hv=0;
        for(int i=0;s[i];i++){
             hv=0;
            for(int j=0;j<k;j++){
                hv+=s[i]-'a';
                i++;
            }
            i--;
            hv%=26;
            ans+='a'+hv;
        }
        return ans;
    }
};