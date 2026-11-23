# Product of the Last K Numbers
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Design, Data Stream, Prefix Sum

"""
This algorithm maintains a list of running prefix products (initialized with `1`) so that `getProduct(k)` can compute the product of the last `k` numbers by dividing the latest prefix product by the product `k` positions earlier. When `0` is added, the prefix list resets to `[1]`, allowing `getProduct(k)` to immediately return `0` whenever `k` is greater than or equal to the current list length (indicating a zero occurred within the last `k` elements). Both `add` and `getProduct` run in $O(1)$ time, and the space complexity is $O(n)$ in the worst case, where $n$ is the number of `add` operations since the last zero.
"""

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]