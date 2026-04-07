1class Solution {
2public:
3    int dif[5]={0,1,0,-1,0};
4    int dfs(int r,int c,int R,int C,vector<vector<int>>& grid,vector<vector<int>>& dp){    
5        dp[r][c]=1;
6        int area=1;
7        for(int i=0;i<4;i++){
8            int ar=r+dif[i],ac=c+dif[i+1];
9            if(ar>=0 && ac>=0 && ar<R && ac<C && grid[ar][ac]==1 && !dp[ar][ac]){
10                area+=dfs(ar,ac,R,C,grid,dp);
11            }
12        }
13        
14        return area;
15    }
16    int maxAreaOfIsland(vector<vector<int>>& grid) {
17        int R=grid.size(),C=grid[0].size();
18        vector<vector<int>>dp(R,vector<int>(C,0));
19        int ans=0;
20        for(int r=0;r<R;r++){
21            for(int c=0;c<C;c++){
22                if(grid[r][c]==1 && !dp[r][c]){ 
23                ans=max(ans,dfs(r,c,R,C,grid,dp));}
24            }
25        }
26        return ans;
27    }
28};