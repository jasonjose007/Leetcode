class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        unordered_map<char, string> phone = {
            {'2',"abc"}, {'3',"def"}, {'4',"ghi"}, {'5',"jkl"},
            {'6',"mno"}, {'7',"pqrs"}, {'8',"tuv"}, {'9',"wxyz"}
        };

        vector<string> result;
        string current;

        function<void(int)> backtrack = [&](int idx) {
            if (idx == digits.size()) {
                result.push_back(current);
                return;
            }
            for (char c : phone[digits[idx]]) {
                current += c;
                backtrack(idx + 1);
                current.pop_back();  // undo
            }
        };

        backtrack(0);
        return result;
    }
};