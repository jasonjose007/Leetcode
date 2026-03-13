1class Solution {
2public:
3    vector<string> fizzBuzz(int n) {
4        vector<string>ans(n);
5        for(int i=0;i<n;i++){
6            int num=i+1;
7            if(num%15==0) ans[i]="FizzBuzz";
8            else if(num%5==0) ans[i]="Buzz";
9            else if(num%3==0) ans[i]="Fizz";
10            else ans[i]=to_string(num);
11        }
12        return ans;
13    }
14};