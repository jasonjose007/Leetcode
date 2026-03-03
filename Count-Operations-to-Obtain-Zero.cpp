1class Solution {
2public:
3    int countOperations(int num1, int num2) {
4        int count=0;
5        while(num1!=0&&num2!=0){
6            if(num1>num2){
7                num1=num1-num2;
8                count++;
9            }
10            else{
11                num2=num2-num1;
12                count++;
13            }
14        }
15    return count;
16    }
17};