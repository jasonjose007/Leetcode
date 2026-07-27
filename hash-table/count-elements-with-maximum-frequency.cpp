class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int> freq;
        int maxF = 0;
        int countMax = 0;

        for (int x : nums) {
            freq[x]++;

            if (freq[x] == maxF) {
                countMax++;
            } 
            else if (freq[x] > maxF) {
                maxF = freq[x];
                countMax = 1;
            }
        }
        return maxF * countMax;
    }
};