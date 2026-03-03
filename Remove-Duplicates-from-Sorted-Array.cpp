1class Solution {
2public:
3    int removeDuplicates(vector<int>& nums) {
4
5        int unique = 0;
6        int n = nums.size();
7
8        for (int i = 1; i < n; i++) {
9            if (nums[unique] != nums[i]) {
10                unique++;
11                nums[unique] = nums[i];
12            }
13        }
14
15        return unique + 1;
16    }
17};