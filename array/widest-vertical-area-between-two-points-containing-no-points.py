# Widest Vertical Area Between Two Points Containing No Points
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Sorting

"""
This solution extracts and sorts the unique x-coordinates of all points to analyze them along the x-axis, effectively ignoring the y-coordinates since vertical areas depend solely on horizontal distance. It then iterates through the sorted x-coordinates to find the maximum difference between any two adjacent values. The time complexity is $O(N \log N)$ due to sorting the unique x-coordinates (where $N$ is the number of points), and the space complexity is $O(N)$ to store the coordinates.
"""

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_coords = sorted(set(p[0] for p in points))
        max_width = 0
        for i in range(1, len(x_coords)):
            if x_coords[i] - x_coords[i-1] > max_width:
                max_width = x_coords[i] - x_coords[i-1]
        return max_width