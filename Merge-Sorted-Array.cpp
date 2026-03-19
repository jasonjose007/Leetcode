1class Solution {
2public:
3    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
4        for (int j = 0, i = m; j<n; j++){
5            nums1[i] = nums2[j];
6            i++;
7        }
8        sort(nums1.begin(),nums1.end());
9    }
10};