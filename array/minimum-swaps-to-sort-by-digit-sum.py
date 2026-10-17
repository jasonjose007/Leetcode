# Minimum Swaps to Sort by Digit Sum
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, Sorting

"""
This algorithm pairs each number with its digit sum and original index, then sorts the list to determine the target sorted order based on digit sums (and values for ties). It then treats the movement of elements to their target positions as a graph of permutation cycles, traversing each unvisited cycle to sum `cycle_size - 1` swaps. The overall time complexity is $O(N \log N)$ due to the sorting step, and the space complexity is $O(N)$ to store the indexed array and visitation tracking state.
"""

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        indexed_nums = [(digit_sum(val), val, i) for i, val in enumerate(nums)]
        indexed_nums.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps