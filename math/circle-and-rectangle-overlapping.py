# Circle and Rectangle Overlapping
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Geometry

"""
This solution works by first finding the coordinates of the point on the rectangle that is closest to the circle's center using `clamp` logic (`max` and `min`). It then calculates the squared Euclidean distance between this nearest point and the circle's center, comparing it to the squared radius to determine if they overlap. The time complexity is $O(1)$ and the space complexity is $O(1)$ as it only uses a few arithmetic operations and constant extra space.
"""

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        
        return dx * dx + dy * dy <= radius * radius