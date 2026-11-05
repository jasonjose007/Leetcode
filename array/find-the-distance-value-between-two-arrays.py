# Find the Distance Value Between Two Arrays
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Two Pointers, Binary Search, Sorting

"""
This algorithm sorts `arr2` and then uses binary search for each element in `arr1` to efficiently check if any element in `arr2` falls within the distance threshold `d`. If no such element is found, the element from `arr1` is considered valid and the count is incremented. The time complexity is $O(m \log m + n \log m)$ (where $n$ and $m$ are the lengths of `arr1` and `arr2`), and the space complexity is $O(1)$ or $O(\log m)$ depending on the sorting algorithm's implementation.
"""

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            low = 0
            high = len(arr2) - 1
            valid = True
            while low <= high:
                mid = (low + high) // 2
                if abs(arr2[mid] - x) <= d:
                    valid = False
                    break
                elif arr2[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            if valid:
                count += 1
        return count