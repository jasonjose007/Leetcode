# Fair Candy Swap
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Binary Search, Sorting

"""
This solution calculates the total candy sums for both Alice and Bob to find the target difference each must exchange. It then converts Bob's candy sizes into a hash set for $O(1)$ lookups and iterates through Alice's candies to find a value $y$ in Bob's set that satisfies the equation $y = x - \text{diff}$. The time complexity is $O(N + M)$ to compute sums, build the set, and search it, while the space complexity is $O(M)$ to store Bob's sizes in the set (where $N$ and $M$ are the lengths of Alice's and Bob's lists).
"""

class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_a - sum_b) // 2
        set_b = set(bobSizes)
        
        for x in aliceSizes:
            y = x - diff
            if y in set_b:
                return [x, y]