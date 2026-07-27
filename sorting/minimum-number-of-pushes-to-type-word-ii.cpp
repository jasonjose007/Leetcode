class Solution {
public:
    int minimumPushes(string word) {
        vector<int>fq(26,0);
        for(char ch:word){
            fq[ch-'a']++;
        } 
        int ans=0,count=0;
        for(int i=0;i<26;i++){
            for(int j=i+1;j<26;j++){
                if(fq[i]<fq[j]){
                    int temp=fq[i];
                    fq[i]=fq[j];
                    fq[j]=temp;
                }
            }
        }
        for(int i=0;i<26;i++){
            count++;
            ans+=(i/8+1)*fq[i];
        }
        return ans;
    }
};