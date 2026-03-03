1class Solution {
2public:
3    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
4      int max=-1;
5      vector <bool> ans;
6      for(int i=0;i<candies.size();i++){
7        if(candies[i]>max){
8            max=candies[i];
9        }
10    }
11    for(int i=0;i<candies.size();i++){
12    int sum=candies[i]+extraCandies;
13    if(sum>=max){
14        ans.push_back(1);}
15    else{
16        ans.push_back(0);}
17    }
18    return ans;
19    }
20};