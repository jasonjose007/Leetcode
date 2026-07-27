class Solution {
public:
    int minimumCost(vector<int>& cost) {
        int ans=0;
        if(cost.size()<2) return cost[0];
        sort(cost.begin(),cost.end());
        for(int i=cost.size()-1;i>=0;i--){
           if(i-1<0) ans+=cost[i];
           else ans+=cost[i]+cost[i-1];
           i-=2;
        }
        return ans;
    }
};