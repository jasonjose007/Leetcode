class Solution {
public:
    int digitFrequencyScore(int n) {
        int score=0;
        unordered_map<int,int>mp;
        while(n!=0){
            mp[n%10]++;
            n/=10;
        }
        for(auto pair:mp){
            score+=pair.first*pair.second;
        }
        return score;
    }
};