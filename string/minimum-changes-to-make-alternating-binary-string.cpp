class Solution {
public:
    int minOperations(string s) {
        int p1 = 0;
        int p2 = 0;
        
        for(int i = 0; i < s.length(); i++) {
            if(i % 2 == 0) {
                if(s[i] != '0') p1++;
                if(s[i] != '1') p2++;
            }
            else {
                if(s[i] != '1') p1++;
                if(s[i] != '0') p2++;
            }
        }
        
        return min(p1, p2);
    }
};