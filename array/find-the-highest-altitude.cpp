class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> alt(gain.size()+1,0);
        for(int i=0;i<gain.size();i++)
            alt[i+1]=gain[i]+alt[i];
        sort(alt.begin(),alt.end());
        return alt[alt.size()-1];
    }
};