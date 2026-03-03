1class Solution {
2public:
3    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
4        vector<int> ans;
5        for(int i=0;i<nums.size();i++)
6        {
7        int count=0;
8        for(int j=0;j<nums.size();j++)
9        {
10        if(nums[i]>nums[j])
11                count++;
12        }
13        ans.push_back(count);
14        }
15return ans;
16    }
17};