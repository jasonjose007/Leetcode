1class Solution {
2public:
3    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
4for(int i=0;i<names.size();i++){
5for(int j=i+1;j<names.size();j++){
6if(heights[i]<heights[j]){
7int temp=heights[i];
8heights[i]=heights[j];
9heights[j]=temp;
10string temp1=names[i];
11names[i]=names[j];
12names[j]=temp1;
13}
14}
15}
16return names;
17}
18};