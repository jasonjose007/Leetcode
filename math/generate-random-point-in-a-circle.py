# Generate Random Point in a Circle
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Geometry, Rejection Sampling, Randomized

"""
This solution uses the **polar coordinate transformation** method, generating a random angle ($\theta$) uniformly and scaling the radius by the square root of a uniform random number ($\sqrt{u}$) to ensure a uniform distribution of points across the circle's area. The time complexity is $O(1)$ per point generation, and the space complexity is $O(1)$ to store the circle's parameters.
"""

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        theta = random.uniform(0, 2 * math.pi)
        r = self.radius * math.sqrt(random.uniform(0, 1))
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]