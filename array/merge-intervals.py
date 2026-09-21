# Merge Intervals
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Sorting, Quicksort

"""
This solution first sorts the intervals by their start times to ensure they are evaluated in chronological order. It then iterates through the sorted intervals, maintaining a `merged` list where it either extends the end time of the most recent interval if there is an overlap, or appends the current interval as a new entry if there is none. The time complexity is $O(N \log N)$ due to the initial sorting step, and the space complexity is $O(N)$ to store the resulting merged intervals.
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged