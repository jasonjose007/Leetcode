1class Solution {
2public:
3    bool isHappy(int n) {
4        if(n==1 || n==7) return true;
5        else if(n<10) return false;
6        else{
7            int sum=0;
8            while(n>0){
9                int temp=n%10;
10                sum+= temp*temp;
11                n=n/10;
12            }
13            return isHappy(sum);
14        }
15    }
16};