1class Solution {
2public:
3    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
4        int count = 0;
5        int size = flowerbed.size();
6
7        for(int i = 0; i < size; i++) {
8
9            if(flowerbed[i] == 0) {
10
11                int left = (i == 0) ? 0 : flowerbed[i-1];
12                int right = (i == size-1) ? 0 : flowerbed[i+1];
13
14                if(left == 0 && right == 0) {
15                    flowerbed[i] = 1;
16                    count++;
17                }
18            }
19
20            if(count >= n) return true;
21        }
22
23        return false;
24    }
25};