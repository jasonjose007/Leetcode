1class Solution {
2public:
3    long long gcdSum(vector<int>& nums) {
4        vector<int>pgcd(nums.size());
5        int maxi=nums[0];
6        for(int i=0;i<nums.size();i++){
7            if(nums[i]>maxi) maxi=nums[i];
8            pgcd[i]= __gcd(maxi,nums[i]);
9            
10        }
11        sort(pgcd.begin(),pgcd.end());
12        long long int sum=0;
13        int i=0,j=nums.size()-1;
14        while(i<j){
15            sum+=__gcd(pgcd[i],pgcd[j]);
16            i++;
17            j--;
18        }
19        return sum;
20    }
21};