1class Solution {
2public:
3    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
4        int count=0;
5        for(int i=0;i<hours.size();i++)
6        {
7            if(hours[i]>=target)
8            count++;
9        }
10    return count;
11    }
12};