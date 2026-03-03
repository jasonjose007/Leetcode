1class Solution {
2public:
3    void moveZeroes(vector<int>& nums) {
4
5        int n = nums.size();
6        int non_zero = 0;
7
8        for (int i = 0; i < n; i++) {
9
10            if (nums[i] != 0) {
11                swap(nums[non_zero], nums[i]);
12                non_zero++;
13            } else if (nums[i] == 0) {
14                continue;
15            }
16        }
17
18        return;
19    }
20};
21
22