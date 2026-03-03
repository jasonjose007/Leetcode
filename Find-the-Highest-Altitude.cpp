1class Solution {
2public:
3    int largestAltitude(vector<int>& gain) {
4        vector<int> alt(gain.size()+1,0);
5        for(int i=0;i<gain.size();i++)
6            alt[i+1]=gain[i]+alt[i];
7        sort(alt.begin(),alt.end());
8        return alt[alt.size()-1];
9    }
10};