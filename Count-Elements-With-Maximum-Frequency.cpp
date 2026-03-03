1class Solution {
2public:
3    int maxFrequencyElements(vector<int>& nums) {
4        unordered_map<int,int> freq;
5        int maxF = 0;
6        int countMax = 0;
7
8        for (int x : nums) {
9            freq[x]++;
10
11            if (freq[x] == maxF) {
12                countMax++;
13            } 
14            else if (freq[x] > maxF) {
15                maxF = freq[x];
16                countMax = 1;
17            }
18        }
19        return maxF * countMax;
20    }
21};