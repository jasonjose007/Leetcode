1class Solution {
2public:
3    vector<int> buildArray(vector<int>& nums) {
4        vector<int> ans;
5        for(int i=0;i<nums.size();i++)
6        ans.push_back(nums[nums[i]]);
7    return ans;
8    }
9};