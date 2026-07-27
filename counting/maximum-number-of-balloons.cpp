class Solution {
public:
    int maxNumberOfBalloons(string text) {
         std::map<char, int> etalon{
            {'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}};

        std::map<char, int> temp {
            {'b', 0}, {'a', 0}, {'l', 0}, {'o', 0}, {'n', 0}};
        
        for (int i = 0; i < text.size(); i++){
            temp[text[i]] = temp[text[i]] + 1;
        }
        
        int count = 0;
        char* balon = "balon";
        while(true) {
            for (int i = 0; i < 5; i++) {
                temp[balon[i]] -= etalon[balon[i]];
                if (temp[balon[i]] < 0)
                    return count;
            }
            count++;
        }
    }
};