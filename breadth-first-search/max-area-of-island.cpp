class Solution {
public:
    int dif[5]={0,1,0,-1,0};
    int dfs(int r,int c,int R,int C,vector<vector<int>>& grid,vector<vector<int>>& dp){    
        dp[r][c]=1;
        int area=1;
        for(int i=0;i<4;i++){
            int ar=r+dif[i],ac=c+dif[i+1];
            if(ar>=0 && ac>=0 && ar<R && ac<C && grid[ar][ac]==1 && !dp[ar][ac]){
                area+=dfs(ar,ac,R,C,grid,dp);
            }
        }
        
        return area;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int R=grid.size(),C=grid[0].size();
        vector<vector<int>>dp(R,vector<int>(C,0));
        int ans=0;
        for(int r=0;r<R;r++){
            for(int c=0;c<C;c++){
                if(grid[r][c]==1 && !dp[r][c]){ 
                ans=max(ans,dfs(r,c,R,C,grid,dp));}
            }
        }
        return ans;
    }
};