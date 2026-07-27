class Solution {
public:
    int mirrorFrequency(string s) {
        unordered_map<char, int> mp;
        int sum = 0;
        for (char ch : s)
            mp[ch]++;
        for (char ch : s) {
            char mir;
            if (isalpha(ch))
                mir = (char)('z' - (ch - 'a'));
            else
                mir = (char)('9' - (ch - '0'));
            if (mp.find(mir) != mp.end()) {
                sum += abs(mp[ch] - mp[mir]);
                mp[ch] = 0;
                mp[mir] = 0;
            } else {
                sum += mp[ch];
                mp[ch] = 0;
            }
        }
        return sum;
    }
};