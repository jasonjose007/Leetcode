# Combination Sum
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Backtracking

"""
This solution uses a backtracking algorithm implemented via Depth-First Search (DFS) to explore all possible combinations of candidates. It iterates through the sorted array, recursively subtracting the current candidate from the target while allowing reuse of the same element (by passing index `i` instead of `i + 1`) and pruning branches where the candidate exceeds the remaining target. The time complexity is $O(N^{T/M})$, where $N$ is the number of candidates, $T$ is the target, and $M$ is the minimum candidate value, while the space complexity is $O(T/M)$ to store the recursion stack and current path.
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                dfs(remain - candidates[i], i, path)
                path.pop()

        dfs(target, 0, [])
        return res