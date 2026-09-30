# Combination Sum II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Backtracking

"""
This solution uses a backtracking algorithm combined with sorting to find all unique combinations that sum to the target. By sorting the candidates and skipping duplicate values at the same recursion level (`if i > start and candidates[i] == candidates[i - 1]`), it efficiently avoids generating duplicate combinations, while also pruning branches where the candidate exceeds the remaining target. The time complexity is $O(2^n)$ in the worst case due to the exponential number of subsets, and the space complexity is $O(n)$ to store the recursion stack and current path.
"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        
        def backtrack(start: int, target: int, path: list[int]):
            if target == 0:
                res.append(list(path))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return res