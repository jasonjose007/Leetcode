# Longest Harmonious Subsequence
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Sliding Window, Sorting, Counting

"""
This solution uses a frequency map (`Counter`) to count the occurrences of each number in the array and then iterates through the unique keys to check if `num + 1` exists. If the consecutive number is present, it calculates the combined frequency of both numbers and updates the maximum harmonious subsequence length. The time complexity is $O(n)$ to build the frequency map and iterate through the unique elements, and the space complexity is $O(n)$ to store the counts in the hash map.
"""

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_len = 0
        for num in counts:
            if num + 1 in counts:
                max_len = max(max_len, counts[num] + counts[num + 1])
        return max_len