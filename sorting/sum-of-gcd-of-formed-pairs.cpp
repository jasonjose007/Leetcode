class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        vector<int>pgcd(nums.size());
        int maxi=nums[0];
        for(int i=0;i<nums.size();i++){
            if(nums[i]>maxi) maxi=nums[i];
            pgcd[i]= __gcd(maxi,nums[i]);
            
        }
        sort(pgcd.begin(),pgcd.end());
        long long int sum=0;
        int i=0,j=nums.size()-1;
        while(i<j){
            sum+=__gcd(pgcd[i],pgcd[j]);
            i++;
            j--;
        }
        return sum;
    }
};