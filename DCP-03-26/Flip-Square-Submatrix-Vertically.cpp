1class Solution {
2public:
3    static vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
4        for(int t=x, b=x+k-1; t<b; t++, b--){
5            for(int j=y; j<y+k; j++)
6                swap(grid[t][j], grid[b][j]);
7        }
8        return grid;
9    }
10};