class Solution {
public:
    int reverseDegree(string s) {
     int sum=0;
     for(int i=0;s[i];i++){
     int val=(s[i]-'a');
     sum+=(i+1)*abs(26-val);}
    return sum;
    }
};