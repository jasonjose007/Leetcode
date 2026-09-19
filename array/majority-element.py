# Majority Element
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm

"""
This solution implements the **Boyer-Moore Voting Algorithm**, which tracks a `candidate` and a `count` that increments for matching elements and decrements for differing ones, reassigning the candidate whenever the count drops to zero. Because the majority element appears more than $\lfloor n/2 \rfloor$ times, its occurrences will always outweigh all other elements combined, ensuring it remains the final candidate. This approach achieves an optimal time complexity of **$O(n)$** with **$O(1)$** auxiliary space.
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate