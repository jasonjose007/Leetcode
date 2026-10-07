# Water and Jug Problem
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Depth-First Search, Breadth-First Search, Bézout's Lemma, Euclidean Algorithm, Greatest Common Divisor, Extended Euclidean Algorithm

"""
This solution uses a mathematical approach based on Bézout's identity from number theory, which states that an exact amount of water can be measured if and only if the `target` is a multiple of the greatest common divisor (GCD) of the two jug capacities, `x` and `y`. The algorithm first checks basic edge cases (such as when the total capacity of both jugs is less than the target), and then simply computes `target % math.gcd(x, y) == 0`. The time complexity is $O(\log(\min(x, y)))$ due to the Euclidean algorithm used for computing the GCD, and the space complexity is $O(1)$ as it uses a constant amount of extra space.
"""

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if x == target or y == target or x + y == target:
            return True
        return target % math.gcd(x, y) == 0