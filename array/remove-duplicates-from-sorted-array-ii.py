# Remove Duplicates from Sorted Array II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Two Pointers

"""
This two-pointer algorithm iterates through the sorted array and writes the current element `x` to index `k` only if fewer than two elements have been kept (`k < 2`) or if `x` differs from the element placed two positions back (`nums[k - 2]`). Because the array is sorted, this check guarantees that no value is duplicated more than twice while modifying the array in place. The solution runs in **$O(n)$ time**, where $n$ is the length of `nums`, and uses **$O(1)$ auxiliary space**.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k