class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int cs=0,max=0;
        for(int val:nums){
            if(val==0){
                if(cs>max){
                    max=cs;
                }
                cs=0;
                continue;
            }
            cs++;
        }
        if(cs>max){
            max=cs;
        }
        return max;
    }
};