1class Solution {
2public:
3    int findMaxConsecutiveOnes(vector<int>& nums) {
4        int cs=0,max=0;
5        for(int val:nums){
6            if(val==0){
7                if(cs>max){
8                    max=cs;
9                }
10                cs=0;
11                continue;
12            }
13            cs++;
14        }
15        if(cs>max){
16            max=cs;
17        }
18        return max;
19    }
20};