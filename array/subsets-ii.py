# Subsets II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Backtracking, Bit Manipulation

"""
This solution uses a **backtracking** algorithm combined with sorting to generate all unique subsets. By sorting the input array first, the algorithm can easily skip duplicate adjacent elements at the same recursion level (`if i > start and nums[i] == nums[i - 1]`), ensuring duplicate subsets are avoided. The time complexity is $O(N \cdot 2^N)$ and the space complexity is $O(N)$ for the recursion stack, where $N$ is the number of elements in `nums`.
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        def backtrack(start, current):
            res.append(list(current))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(0, [])
        return res