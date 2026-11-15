# Assign Cookies
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Two Pointers, Greedy, Sorting, Quicksort

"""
This solution uses a **greedy algorithm with two pointers** by first sorting both the children's greed factors (`g`) and the cookie sizes (`s`) in ascending order. It iterates through the cookies to satisfy the least demanding child first, advancing the child pointer `i` only when a cookie is large enough (`s[j] >= g[i]`) while always moving to the next cookie `j`. 

The time complexity is **$O(n \log n + m \log m)$** due to the sorting step (where $n$ and $m$ are the lengths of the input arrays), and the auxiliary space complexity is **$O(1)$** (or $O(\log n + \log m)$ for the memory required by Python's Timsort algorithm).
"""

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        n = len(g)
        m = len(s)
        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i