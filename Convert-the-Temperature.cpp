1class Solution {
2public:
3    vector<double> convertTemperature(double celsius) {
4     vector<double> ans;
5        double k=celsius+273.15;
6        double f=celsius*1.80+32.00;
7        ans.push_back(k);
8        ans.push_back(f);
9        return ans;
10    }
11};