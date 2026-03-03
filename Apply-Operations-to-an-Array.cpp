1class Solution {
2public:
3    vector<int> applyOperations(vector<int>& nums) {
4        const int n=nums.size();
5        for(int i=0; i<n-1; i++){
6            if (nums[i]==nums[i+1]){
7                nums[i]<<=1;
8                nums[i+1]=0;
9                i++;// 0 needs no operation
10            }
11        }
12        int j=0;
13        for(int i=0; i<n; i++){
14            if (nums[i]>0) nums[j++]=nums[i];
15        }
16        fill(nums.begin()+j, nums.end(), 0);
17        return nums;
18    }
19};