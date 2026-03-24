1class Solution {
2public:
3    bool isPalindrome(string s) {
4       int start=0;
5       int end=s.size()-1;
6       while(start<=end){
7           if(!isalnum(s[start])){start++; continue;}
8           if(!isalnum(s[end])){end--;continue;}
9           if(tolower(s[start])!=tolower(s[end]))return false;
10           else{
11               start++;
12               end--;
13           }
14       }
15       return true;
16}
17};