class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
      int max=-1;
      vector <bool> ans;
      for(int i=0;i<candies.size();i++){
        if(candies[i]>max){
            max=candies[i];
        }
    }
    for(int i=0;i<candies.size();i++){
    int sum=candies[i]+extraCandies;
    if(sum>=max){
        ans.push_back(1);}
    else{
        ans.push_back(0);}
    }
    return ans;
    }
};