# Permutations II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Backtracking, Sorting

"""
This solution uses a backtracking algorithm with a frequency map to construct permutations element-by-element, naturally avoiding duplicate permutations by only branching on unique numbers at each step. At each recursive call, it selects an available number, decrements its count, recurses to build the rest of the permutation, and then backtracks by restoring the count and removing the number. The time complexity is $\mathcal{O}(N \cdot \frac{N!}{\prod n_i!})$ (upper-bounded by $\mathcal{O}(N \cdot N!)$) to generate all unique permutations of length $N$, and the auxiliary space complexity is $\mathcal{O}(N)$ for the recursion stack and frequency map.
"""

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        
        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for x in counts:
                if counts[x] > 0:
                    counts[x] -= 1
                    path.append(x)
                    backtrack(path)
                    path.pop()
                    counts[x] += 1
        
        backtrack([])
        return res