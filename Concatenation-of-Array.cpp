1class Solution {
2public:
3    vector<int> getConcatenation(vector<int>& nums) {
4        int n= nums.size();
5        for(int i=0;i<n;i++){
6
7            nums.push_back(nums[i]);
8        }
9        return nums;
10
11    }
12};