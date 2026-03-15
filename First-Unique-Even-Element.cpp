1class Solution {
2public:
3    int firstUniqueEven(vector<int>& nums) {
4        int max=-1;
5        for(int i=0;i<nums.size();i++){
6            if(nums[i]>max){
7                max=nums[i];
8            }
9        }
10        vector<int> freq(max+1,0);
11        for(int i=0;i<nums.size();i++){
12            freq[nums[i]]++;
13        }
14        for(int i=0;i<nums.size();i++){
15            if(nums[i]%2==0&&freq[nums[i]]==1)
16                return nums[i];
17        }
18        return -1;
19    }
20    
21};