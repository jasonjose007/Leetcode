# Subsets
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Backtracking, Bit Manipulation

"""
This solution uses an **iterative cascading** approach, beginning with an empty subset and progressively doubling the results by appending the current number to a copy of every existing subset. Both the time and space complexity are **$O(n \cdot 2^n)$**, where $n$ is the number of elements in `nums`, because $2^n$ total subsets are generated and each requires up to $O(n)$ operations and memory to copy and store.
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res