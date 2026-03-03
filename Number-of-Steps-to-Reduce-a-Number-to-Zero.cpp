1class Solution {
2public:
3    int numberOfSteps(int num) {
4        int count=0;
5        while(num>0){
6            if(num%2==0){
7                num/=2;
8            }
9            else{
10                num--;
11            }
12            count++;
13        }
14        return count;
15    }
16};