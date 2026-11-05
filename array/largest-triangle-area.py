# Largest Triangle Area
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Math, Geometry, Polygons

"""
This solution uses a brute-force approach with three nested loops to examine every possible combination of three distinct points from the given set. For each combination, it calculates the triangle's area using the Shoelace formula (determinant method) and keeps track of the maximum area found. The algorithm has a time complexity of $O(n^3)$ and a space complexity of $O(1)$, where $n$ is the number of points.
"""

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        max_area = 0.0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    if area > max_area:
                        max_area = area
        return max_area