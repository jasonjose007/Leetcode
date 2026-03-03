1double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2,
2                              int nums2Size) {
3    int m = nums1Size, n = nums2Size;
4    int p1 = 0, p2 = 0;
5    int getMin() {
6        if (p1 < m && p2 < n) {
7            return nums1[p1] < nums2[p2] ? nums1[p1++] : nums2[p2++];
8        } else if (p1 < m) {
9            return nums1[p1++];
10        } else if (p2 < n) {
11            return nums2[p2++];
12        }
13        return -1;
14    }
15
16    double median;
17    if ((m + n) % 2 == 0) {
18        for (int i = 0; i < ((m + n) / 2) - 1; ++i) {
19            int temp = getMin();
20        }
21        median = (getMin() + getMin()) / 2.0;
22    } else {
23        for (int i = 0; i < (m + n) / 2; ++i) {
24            int temp = getMin();
25        }
26        median = getMin();
27    }
28
29    return median;
30}