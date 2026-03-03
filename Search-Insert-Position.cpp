1class Solution {
2public:
3    int searchInsert(vector<int>& nums, int target) {
4        int length = nums.size();
5        for (int i = 0; i < length; ++i) {
6            if (nums[i] >= target) {
7                return i;
8            }
9        }
10        return length;
11    }
12};