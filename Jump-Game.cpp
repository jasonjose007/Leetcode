1class Solution {
2public:
3    bool canJump(vector<int>& nums) {
4        int till=0;
5        for(int i=0;i<nums.size();i++){
6            if(i>till) return 0;
7            till=max(till,i+nums[i]);
8        }
9        return 1;
10    }
11};