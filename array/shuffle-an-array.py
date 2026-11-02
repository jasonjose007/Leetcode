# Shuffle an Array
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Math, Design, Randomized

"""
This solution uses the **Fisher-Yates shuffle algorithm**, which iterates backward through the array and swaps each element with a randomly chosen element from the preceding unshuffled portion (including itself). This ensures a uniformly random permutation of the array. The time complexity is $O(n)$ for the shuffle and reset operations, and the space complexity is $O(n)$ to store both the original and working copies of the array.
"""

class Solution:

    def __init__(self, nums: list[int]):
        self.original = list(nums)
        self.nums = list(nums)

    def reset(self) -> list[int]:
        self.nums = list(self.original)
        return self.nums

    def shuffle(self) -> list[int]:
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums