class Solution {
public:
    int firstUniqueEven(vector<int>& nums) {
        int max=-1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]>max){
                max=nums[i];
            }
        }
        vector<int> freq(max+1,0);
        for(int i=0;i<nums.size();i++){
            freq[nums[i]]++;
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i]%2==0&&freq[nums[i]]==1)
                return nums[i];
        }
        return -1;
    }
    
};