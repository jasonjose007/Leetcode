1class Solution {
2public:
3    int differenceOfSums(int n, int m) {
4        int sum1=0,sum2=0;
5        for(int i=1;i<=n;i++)
6        {
7            if(i%m!=0)
8                sum1+=i;
9            else
10                sum2+=i;
11        }
12        return sum1-sum2;
13    }
14};