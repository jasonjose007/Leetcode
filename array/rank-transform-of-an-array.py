# Rank Transform of an Array
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting

"""
The algorithm extracts and sorts the unique elements of the input array, then maps each distinct value to its 1-based rank using a hash map. It then reconstructs the array by replacing each original element with its corresponding rank looked up from the map. This approach runs in **$O(N \log N)$ time** due to sorting and uses **$O(N)$ auxiliary space** to store the unique elements and the rank map, where $N$ is the length of the array.
"""

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique = sorted(list(set(arr)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        return [rank_map[x] for x in arr]