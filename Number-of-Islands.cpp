1class Solution {
2public:
3    int diff[5]={0,1,0,-1,0};
4    void dfs(int r,int c,int R,int C,vector<vector<char>>&grid , vector<vector<int>>& dp){
5        dp[r][c]=1;
6        for(int di=0;di<4;di++){
7            int ar=r+diff[di],ac=c+diff[di+1];
8            if(ar>=0 && ac>=0 && ar<R && ac<C && dp[ar][ac]!=1 && grid[ar][ac]=='1'){
9                  dfs(ar,ac,R,C,grid,dp);
10            }
11        }
12    }
13    int numIslands(vector<vector<char>>& grid) {
14        int R=grid.size(),C=grid[0].size(),ic=0;
15        vector<vector<int>>dp(R,vector<int>(C,0));
16        for(int r=0;r<R;r++){
17            for(int c=0;c<C;c++){
18                if(!dp[r][c] && grid[r][c]=='1'){
19                    dfs(r,c,R,C,grid,dp);
20                    ic++;
21                }
22            }
23        }
24        return ic;
25    }
26};