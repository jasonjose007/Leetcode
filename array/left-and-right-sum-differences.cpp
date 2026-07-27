class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
       vector<int> leftsum(nums.size(),0) ;
       vector<int> rightsum(nums.size(),0);
       int lcurrsum=0,rcurrsum=0;
       
       for(int i=0;i<nums.size()-1;i++){
            lcurrsum+=nums[i];
            leftsum[i+1]=lcurrsum;
       }
       for(int i=nums.size()-1;i>0;i--){
            rcurrsum+=nums[i];
            rightsum[i-1]=rcurrsum;
       }
       for(int i=0;i<nums.size();i++){
        leftsum[i]=abs(leftsum[i]-rightsum[i]);
       }
       return leftsum;
    }
};