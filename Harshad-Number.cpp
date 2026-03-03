1class Solution {
2public:
3    int sumOfTheDigitsOfHarshadNumber(int x) {
4        int temp=x,sum=0;
5        while(temp>0){
6            sum+=temp%10;
7            temp/=10;
8        }
9        if(x%sum==0)
10            return sum;
11        return -1;
12    }
13};