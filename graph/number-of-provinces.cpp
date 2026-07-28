class Solution {
public:
    int find(vector<int>&leader,int node){
        if(leader[node]!=node)leader[node]=find(leader,leader[node]);
        return leader[node];
    }
    void join(vector<int>&leader,int left,int right){
        leader[find(leader,right)]=find(leader,left);
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int N=isConnected.size();
        vector<int>leader(N+1);
        for(int i=0;i<N+1;i++) leader[i]=i;
        for(int l=0;l<N;l++){
            for(int r=0;r<N;r++){
                if(isConnected[l][r]){
                    join(leader,l+1,r+1);
                }
            }
        }
        vector<int>grp(N+1,0);
        for(int i=1;i<=N;i++){
            grp[find(leader,i)]++;
        }
        int cnt=0;
        for(int i=0;i<=N;i++){
            if(grp[i]!=0) cnt++;
        }
        return cnt;
    }
};