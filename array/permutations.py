# Permutations
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Backtracking

"""
This solution uses a **backtracking** algorithm to recursively build all possible permutations by choosing one element at a time from the remaining available options. When a permutation reaches the same length as the input list, it is added to the result array. The time complexity is **$O(n \cdot n!)$** and the space complexity is **$O(n!)$** to store and generate all $n!$ permutations of length $n$.
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(path, options):
            if not options:
                res.append(path[:])
                return
            for i in range(len(options)):
                path.append(options[i])
                backtrack(path, options[:i] + options[i+1:])
                path.pop()
        backtrack([], nums)
        return res