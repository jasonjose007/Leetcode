1class Solution {
2public:
3    bool isAll9(vector<int>& digits){
4        bool ans=1;
5        for(int d: digits)
6            ans=( ans & d==9);
7        return ans;
8    }
9
10    vector<int> plusOne(vector<int>& digits) {
11        int n=digits.size();
12        if (isAll9(digits))
13        {
14            digits.assign(n+1, 0);
15            digits[0]=1;
16            return digits;
17        }
18        else
19        {
20            digits[n-1]++;
21            if (digits[n-1]!=10) return digits;
22            else {
23                digits.pop_back();
24                digits=plusOne(digits);
25                digits.push_back(0);
26                return digits;
27            }
28        }
29    }
30};