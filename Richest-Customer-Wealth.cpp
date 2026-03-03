1class Solution {
2public:
3    int maximumWealth(vector<vector<int>>& accounts) {
4        int max=-1;
5        for(int i=0;i<accounts.size();i++)
6        {
7            int sum=0;
8            for(int j=0;j<accounts[i].size();j++)
9            {
10                sum+=accounts[i][j];
11            }
12            if(sum>max)
13            max=sum;
14        }
15            return max;
16        }
17};