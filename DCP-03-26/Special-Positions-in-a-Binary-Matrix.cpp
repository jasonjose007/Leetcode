1#include <vector>
2using namespace std;
3
4class Solution {
5public:
6    int numSpecial(vector<vector<int>>& mat) {
7        int rows = mat.size();
8        int cols = mat[0].size();
9        int count = 0;
10
11        for(int i = 0; i < rows; i++) {
12            for(int j = 0; j < cols; j++) {
13                
14                if(mat[i][j] == 1) {
15                    
16                    int rowOnes = 0;
17                    int colOnes = 0;
18                    for(int k = 0; k < cols; k++) {
19                        if(mat[i][k] == 1)
20                            rowOnes++;
21                    }
22                    for(int k = 0; k < rows; k++) {
23                        if(mat[k][j] == 1)
24                            colOnes++;
25                    }
26
27                    if(rowOnes == 1 && colOnes == 1)
28                        count++;
29                }
30            }
31        }
32
33        return count;
34    }
35};