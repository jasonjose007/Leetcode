1class Solution {
2public:
3    static int countPrimeSetBits(int left, int right) {
4        int prime[]={2, 3, 5, 7, 11, 13, 17, 19};
5        bitset<21> isPrime=0;
6        for(int p: prime) isPrime[p]=1;
7        int sum=0;
8        for(unsigned i=left; i<=right; i++){
9            int b=popcount(i);
10            if (isPrime[b]) sum++;
11        }
12        return sum;
13    }
14};