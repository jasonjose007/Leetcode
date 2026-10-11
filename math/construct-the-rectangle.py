# Construct the Rectangle
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math

"""
The algorithm initializes the width $W$ to $\lfloor\sqrt{\text{area}}\rfloor$ and decrements it until finding the largest factor less than or equal to the square root. It then calculates the length as $L = \text{area} // W$, naturally satisfying $L \ge W$ while minimizing the difference $L - W$. This approach runs in $O(\sqrt{\text{area}})$ worst-case time complexity (occurring when `area` is a prime number) and uses $O(1)$ auxiliary space.
"""

class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w = int(area**0.5)
        while area % w != 0:
            w -= 1
        return [area // w, w]