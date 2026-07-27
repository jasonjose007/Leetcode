class Solution {
public:
    vector<int> helper(string s, int n) {
        int len = 0;
        int i = 1;
        vector<int> lps(n, 0);

        lps[0] = 0;
        while(i < n) {
            if(s[i] == s[len]) {
                len++;
                lps[i] = len;
                i++;
            }
            else {
                if(len != 0) {
                    len = lps[len - 1];
                }
                else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    bool repeatedSubstringPattern(string s) {
        int n = s.length();
        vector<int> lps = helper(s, n);

        int ans = lps[n-1];

        if (ans > 0 && n % (n - ans) == 0) {
            return true;
        }
        return false;
    }
};