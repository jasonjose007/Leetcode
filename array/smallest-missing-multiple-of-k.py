# Smallest Missing Multiple of K
# Difficulty: Easy
# Topics: Array, Hash Table

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        multiple = k
        while multiple in num_set:
            multiple += k
        return multiple