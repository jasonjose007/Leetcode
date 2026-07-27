class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
       sort(nums.begin(),nums.end());
       vector<vector<int>>ans;
       for(int i=0;i<nums.size();i++){
           int t=2;
           vector<int>temp;
           temp.push_back(nums[i]);
           while(t--){
             i++;
            temp.push_back(nums[i]);
           
           }
           if(temp[2]-temp[0]>k) return {};
           ans.push_back(temp);
       } 
       return ans;
    }
};