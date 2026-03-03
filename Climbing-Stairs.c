1int climbStairs(int n) {
2    if (n <= 2) return n;
3    
4    int prev2 = 1;
5    int prev1 = 2;
6    int current;
7    
8    for (int i = 3; i <= n; i++) {
9        current = prev1 + prev2;
10        prev2 = prev1;
11        prev1 = current;
12    }
13    
14    return prev1;
15}