# 4Sum
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Two Pointers, Sorting

"""
This solution sorts the array and uses two nested loops to fix the first two numbers, followed by a two-pointer approach to search for the remaining two elements that complete the target sum. It includes pruning logic—skipping duplicate values and checking boundary sums—to avoid redundant calculations and prevent duplicate quadruplets in the output. The algorithm has a **time complexity of $O(n^3)$** due to the three nested traversal levels and an **auxiliary space complexity of $O(1)$** (or $O(n)$ depending on Python's Timsort implementation, excluding the output array).
"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                    
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res