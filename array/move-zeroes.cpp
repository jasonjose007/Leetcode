class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        int n = nums.size();
        int non_zero = 0;

        for (int i = 0; i < n; i++) {

            if (nums[i] != 0) {
                swap(nums[non_zero], nums[i]);
                non_zero++;
            } else if (nums[i] == 0) {
                continue;
            }
        }

        return;
    }
};

