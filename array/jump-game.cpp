class Solution {
public:
    bool canJump(vector<int>& nums) {
        int till=0;
        for(int i=0;i<nums.size();i++){
            if(i>till) return 0;
            till=max(till,i+nums[i]);
        }
        return 1;
    }
};