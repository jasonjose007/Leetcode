#include <vector>
using namespace std;

class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int rows = mat.size();
        int cols = mat[0].size();
        int count = 0;

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                
                if(mat[i][j] == 1) {
                    
                    int rowOnes = 0;
                    int colOnes = 0;
                    for(int k = 0; k < cols; k++) {
                        if(mat[i][k] == 1)
                            rowOnes++;
                    }
                    for(int k = 0; k < rows; k++) {
                        if(mat[k][j] == 1)
                            colOnes++;
                    }

                    if(rowOnes == 1 && colOnes == 1)
                        count++;
                }
            }
        }

    return count;
    }
};