1int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
2    for (int i = 0; i < numsSize; i++) {
3        for (int j = i + 1; j < numsSize; j++) {
4            if (nums[j] == target - nums[i]) {
5                int* result = malloc(sizeof(int) * 2);
6                result[0] = i;
7                result[1] = j;
8                *returnSize = 2;
9                return result;
10            }
11        }
12    }
13    // Return an empty array if no solution is found
14    *returnSize = 0;
15    return malloc(sizeof(int) * 0);
16}