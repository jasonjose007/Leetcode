1class Solution {
2public:
3    long long gcdSum(vector<int>& nums) {
4        vector<int> velqoradin = nums;
5        int n = velqoradin.size();
6        vector<int> prefixGcd(n);
7        int mx = velqoradin[0];
8        for(int i = 0; i < n; i++){
9            mx = max(mx, velqoradin[i]);
10            prefixGcd[i] = __gcd(velqoradin[i], mx);
11        }
12        sort(prefixGcd.begin(), prefixGcd.end());
13        long long ans = 0;
14        int l = 0, r = n - 1;
15        while(l < r){
16            ans += __gcd(prefixGcd[l], prefixGcd[r]);
17            l++;
18            r--;
19        }
20        return ans;
21    }
22};