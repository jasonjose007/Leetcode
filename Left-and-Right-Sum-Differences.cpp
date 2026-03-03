1class Solution {
2public:
3    vector<int> leftRightDifference(vector<int>& nums) {
4        vector<int> leftsum(nums.size(),0);
5        vector<int> rightsum(nums.size(),0);
6        int lcurrsum=0,rcurrsum=0;
7
8    for(int i=0;i<nums.size()-1;i++){
9        lcurrsum+=nums[i];
10        leftsum[i+1]=lcurrsum;
11    }
12    for(int i=nums.size()-1;i>0;i--){
13        rcurrsum+=nums[i];
14        rightsum[i-1]=rcurrsum;
15    }
16    for(int i=0;i<nums.size();i++){
17        leftsum[i]=abs(leftsum[i]-rightsum[i]);
18    }
19    return leftsum;
20    }
21};