class Solution {
public:
int dr[8]={1,-1,0,0,1,-1,1,-1},dc[8]={0,0,-1,1,1,-1,-1,1};
    queue<pair<int,int>>q;
    
    int bfs(int r, int c, int R, int C,vector<vector<int>>& grid, vector<vector<int>>& dp){
        int path=1;
        dp[r][c]=1;
        q.push({0,0});
        while(q.size()!=0){
            int size=q.size();
            while(size--){
            auto node=q.front();
            q.pop();
            int r=node.first , c= node.second;
            if(r==R-1 && c==C-1) return path;
            for(int i=0;i<8;i++){
                int ar=r +dr[i],ac=c+dc[i];
                if(ar>=0 && ac>=0 && ar<R && ac<C && grid[ar][ac]==0 && !dp[ar][ac]){
                    q.push({ar,ac});
                    dp[ar][ac]=1;
                }
            }
            }
            path++;
        }

        return -1;
    }
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int R=grid.size(),C=grid[0].size();
        vector<vector<int>>dp(R,vector<int>(C,0));
        if(grid[0][0]!=0 || grid[R-1][C-1]!=0) return -1;
        return bfs(0,0,R,C,grid,dp);
    }
};