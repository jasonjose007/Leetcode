# Number of Boomerangs
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Math

"""
The algorithm iterates through each point as a potential pivot and uses a hash map to count the frequencies of squared Euclidean distances to all other points. For each distance occurring $c$ times, it adds $c \times (c - 1)$ to the total to account for every ordered pair that can form a boomerang with that pivot. This approach runs in $O(n^2)$ time complexity due to the nested pairwise iterations and uses $O(n)$ auxiliary space to store distance counts, where $n$ is the number of points.
"""

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        ans = 0
        for p1 in points:
            count = {}
            for p2 in points:
                if p1 == p2:
                    continue
                d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                count[d] = count.get(d, 0) + 1
            for d in count:
                c = count[d]
                ans += c * (c - 1)
        return ans