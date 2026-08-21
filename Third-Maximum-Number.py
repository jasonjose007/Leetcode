# Third Maximum Number
# Difficulty: Easy
# Topics: Array, Sorting

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
            if len(s) > 3:
                s.remove(min(s))
        return min(s) if len(s) == 3 else max(s)