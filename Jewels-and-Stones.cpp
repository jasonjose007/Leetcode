1class Solution {
2public:
3    int numJewelsInStones(string jewels, string stones) {
4     int count=0;
5     for(int i=0;i<jewels.size();i++)
6     {
7        for(int j=0;j<stones.size();j++)
8        {
9            if(jewels[i]==stones[j])
10            count++;
11        }
12     }   
13     return count;
14    }
15};