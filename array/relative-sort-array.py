# Relative Sort Array
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting, Counting Sort, Quicksort, Bubble Sort

"""
This solution counts the frequency of each element in `arr1` using a hash map, then builds the result by
 appending elements in the exact order specified by `arr2`. Any remaining elements not found in `arr2` are collected, sorted in ascending order, and appended to the end of the result. The time complexity is $O(N \log N)$ due to sorting the leftover elements (where $N$ is the size of `arr1`), and the space complexity is $O(N)$ to store the frequency map and output arrays.
"""

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        from collections import Counter
        count = Counter(arr1)
        result = []
        for x in arr2:
            if x in count:
                result.extend([x] * count[x])
                del count[x]
        leftover = []
        for x in count:
            leftover.extend([x] * count[x])
        leftover.sort()
        result.extend(leftover)
        return result