class Solution {
public:
    int dif[5]={0,1,0,-1,0};
    bool dfs(int r,int c,int R,int C,vector<vector<int>>& grid1,vector<vector<int>>& grid2,vector<vector<int>>& dp){
        dp[r][c]=1;
        bool flag=1;
        if(grid1[r][c]!=grid2[r][c]) flag=0;
        for(int di=0;di<4;di++){
            int ar=r+dif[di],ac=c+dif[di+1];
            if(ar>=0 && ac>=0 && ar<R && ac<C && grid2[ar][ac]==1 && !dp[ar][ac]){
                
                flag=dfs(ar,ac,R,C,grid1,grid2,dp)&& flag;
            }
        }
        return flag;
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int R=grid2.size(),C=grid2[0].size(),ic=0;
        vector<vector<int>>dp(R,vector<int>(C,0));
        for(int r=0;r<R;r++){
            for(int c=0;c<C;c++){
                if(grid2[r][c]==1 && !dp[r][c]){
                    if(dfs(r,c,R,C,grid1,grid2,dp)) ic++;
                }
            }
        }
        return ic;
    }
};