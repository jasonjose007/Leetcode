# Contains Duplicate
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting

"""
This solution uses a hash set to track the numbers as they are iterated through the list. For each number, it checks if it already exists in the set (indicating a duplicate); if not, the number is added to the set. The time complexity is **$O(n)$** because set lookups and insertions take $O(1)$ average time, and the space complexity is **$O(n)$** to store up to $n$ unique elements in the set.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False