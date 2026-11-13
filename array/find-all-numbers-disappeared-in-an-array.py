# Find All Numbers Disappeared in an Array
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table

"""
This solution uses an in-place marking algorithm by iterating through the array and using the absolute value of each number as an index, negating the value at that index to mark its presence. A second pass then checks for any remaining positive numbers, whose
 corresponding indices (plus one) represent the missing values. The algorithm achieves $O(n)$ time complexity and $O(1)$ auxiliary space complexity (excluding the output list).
"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
            else:
                nums[i] = -nums[i]
                
        return result