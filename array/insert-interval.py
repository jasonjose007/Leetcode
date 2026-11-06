# Insert Interval
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array

"""
This algorithm iterates through the sorted intervals in three sequential phases: first, it adds all intervals that end before the new interval begins; second, it merges all overlapping intervals by updating the start and end boundaries of the `newInterval`; and finally, it appends the remaining non-overlapping intervals. The time complexity is $
O(n)$ and the space complexity is $O(n)$ to store the resulting list of intervals.
"""

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res