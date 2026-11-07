# Find Right Interval
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Binary Search, Sorting

"""
The algorithm pairs each interval's start time with its original index and sorts them in ascending order. It then iterates through each interval and uses binary search (`bisect_left`) to find the smallest start point greater than or equal to the current interval's end point, returning its original index or `-1` if no valid interval exists. This approach runs in **$O(n \log n)$ time** due to the sorting step and $n$ binary searches, and requires **$O(n)$ auxiliary space** to store the sorted list and the result.
"""

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        from bisect import bisect_left

        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        n = len(intervals)
        ans = []
        for start, end in intervals:
            idx = bisect_left(starts, (end,))
            if idx < n:
                ans.append(starts[idx][1])
            else:
                ans.append(-1)
        return ans