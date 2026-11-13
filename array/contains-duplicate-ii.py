# Contains Duplicate II
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Sliding Window

"""
This solution uses a hash map (`seen`) to store each number and its most recent index as it iterates through the list. For each number, it checks if the number has been seen before and if the difference between its current index and the stored index is less than or equal to $k$. The time complexity is $O(n)$ because it iterates through the list of length $n$ at most once, and the space complexity is $O(n)$ in the worst case to store the elements in the hash map.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False