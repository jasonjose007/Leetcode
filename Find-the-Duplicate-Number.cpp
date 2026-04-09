1class Solution {
2public:
3    int findDuplicate(vector<int>& nums) {
4        unordered_map<int,int>mp;
5        for(int i=0;i<nums.size();i++){
6            if(mp.find(nums[i])!=mp.end()) return nums[i];
7            mp[nums[i]]++;
8        }
9        return 0;
10    }
11};