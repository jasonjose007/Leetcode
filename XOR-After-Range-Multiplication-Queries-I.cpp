1class Solution {
2public:
3    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
4        for(auto q:queries){
5            int l=q[0],r=q[1],k=q[2],v=q[3];
6            for(int idx=l;idx<=r;idx+=k){
7                long long temp=nums[idx];
8                nums[idx]=(temp*v)%(1000000007);
9            }
10        }
11        int sum=0;
12        for(int num:nums){
13            sum^=num;
14        }
15        return sum;
16    }
17};