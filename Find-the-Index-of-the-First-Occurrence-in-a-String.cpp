1class Solution {
2public:
3    int strStr(string haystack, string needle) {
4         size_t pos = haystack.find(needle);
5        return pos == string::npos ? -1 : (int)pos;
6    }
7};