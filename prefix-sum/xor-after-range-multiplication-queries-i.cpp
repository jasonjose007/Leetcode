class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        for(auto q:queries){
            int l=q[0],r=q[1],k=q[2],v=q[3];
            for(int idx=l;idx<=r;idx+=k){
                long long temp=nums[idx];
                nums[idx]=(temp*v)%(1000000007);
            }
        }
        int sum=0;
        for(int num:nums){
            sum^=num;
        }
        return sum;
    }
};