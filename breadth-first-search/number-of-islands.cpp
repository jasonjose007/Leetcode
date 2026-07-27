class Solution {
public:
    int diff[5]={0,1,0,-1,0};
    void dfs(int r,int c,int R,int C,vector<vector<char>>&grid , vector<vector<int>>& dp){
        dp[r][c]=1;
        for(int di=0;di<4;di++){
            int ar=r+diff[di],ac=c+diff[di+1];
            if(ar>=0 && ac>=0 && ar<R && ac<C && dp[ar][ac]!=1 && grid[ar][ac]=='1'){
                  dfs(ar,ac,R,C,grid,dp);
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int R=grid.size(),C=grid[0].size(),ic=0;
        vector<vector<int>>dp(R,vector<int>(C,0));
        for(int r=0;r<R;r++){
            for(int c=0;c<C;c++){
                if(!dp[r][c] && grid[r][c]=='1'){
                    dfs(r,c,R,C,grid,dp);
                    ic++;
                }
            }
        }
        return ic;
    }
};