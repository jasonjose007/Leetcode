1class Solution {
2public:
3int dr[8]={1,-1,0,0,1,-1,1,-1},dc[8]={0,0,-1,1,1,-1,-1,1};
4    queue<pair<int,int>>q;
5    
6    int bfs(int r, int c, int R, int C,vector<vector<int>>& grid, vector<vector<int>>& dp){
7        int path=1;
8        dp[r][c]=1;
9        q.push({0,0});
10        while(q.size()!=0){
11            int size=q.size();
12            while(size--){
13            auto node=q.front();
14            q.pop();
15            int r=node.first , c= node.second;
16            if(r==R-1 && c==C-1) return path;
17            for(int i=0;i<8;i++){
18                int ar=r +dr[i],ac=c+dc[i];
19                if(ar>=0 && ac>=0 && ar<R && ac<C && grid[ar][ac]==0 && !dp[ar][ac]){
20                    q.push({ar,ac});
21                    dp[ar][ac]=1;
22                }
23            }
24            }
25            path++;
26        }
27
28        return -1;
29    }
30    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
31        int R=grid.size(),C=grid[0].size();
32        vector<vector<int>>dp(R,vector<int>(C,0));
33        if(grid[0][0]!=0 || grid[R-1][C-1]!=0) return -1;
34        return bfs(0,0,R,C,grid,dp);
35    }
36};