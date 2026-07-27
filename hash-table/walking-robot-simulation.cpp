class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        map<vector<int>, int> mp;
        vector<int>pos={0,0};
        for (auto vec : obstacles)
            mp[vec] = 1;
        int d = 1,maxdis=0;
        for (int c : commands) {
            if (c == -1) {
                d++;
                if (d > 4)
                    d = 1;
                continue;
            }
            if (c == -2) {
                d--;
                if (d < 1)
                    d = 4;
                continue;
            }
            if (d == 1) {
                while(c--) {
                    pos[1]++;
                    if (mp.find(pos) != mp.end()) {
                        pos[1]--;
                        break;
                    }
                }
                maxdis=max(maxdis,pos[0]*pos[0]+pos[1]*pos[1]);
            }
            if (d == 2) {
                 while(c--){
                    pos[0]++;
                    if (mp.find(pos) != mp.end()) {
                        pos[0]--;
                        break;
                    }
                }
                 maxdis=max(maxdis,pos[0]*pos[0]+pos[1]*pos[1]);
            }
            if (d == 3) {
                 while(c--){
                    pos[1]--;
                    if (mp.find(pos) != mp.end()) {
                        pos[1]++;
                        break;
                    }
                }
                 maxdis=max(maxdis,pos[0]*pos[0]+pos[1]*pos[1]);
            }
            if (d == 4) {
                 while(c--){
                    pos[0]--;
                    if (mp.find(pos) != mp.end()) {
                        pos[0]++;
                        break;
                    }
                }
                 maxdis=max(maxdis,pos[0]*pos[0]+pos[1]*pos[1]);
            }
        }
        return maxdis;
    }
};