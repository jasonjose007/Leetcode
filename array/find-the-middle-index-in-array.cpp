class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int sum=0;
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
        }
        int ls=0,rs=sum;
        for(int i=0;i<nums.size();i++){
            
            if(i==0) ls=0;
            else ls+=nums[i-1];
            rs-=nums[i];    
            if(ls==rs) return i;
            
        }
        return -1;
    }
};