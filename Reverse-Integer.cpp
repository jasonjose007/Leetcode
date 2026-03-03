1class Solution {                      
2public:
3    int reverse(int x) {
4        long r=0;      // decleare r 
5        while(x){
6         r=r*10+x%10; // find remainder and add its to r
7         x=x/10;     // Update the value of x
8        }
9        if(r>INT_MAX || r<INT_MIN) return 0; // check range if r is outside the range then return 0  
10        return int(r);  // if r in the 32 bit range then return r
11    }
12}; 