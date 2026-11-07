# Minimum Subsequence in Non-Increasing Order
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Greedy, Sorting

"""
This algorithm sorts the array in descending order and greedily adds the largest available elements to the subsequence one by one. It maintains the running sum of the chosen elements (`sub_sum`) and the remaining elements (`total_sum`), terminating the loop as soon as `sub_sum` strictly exceeds `total_sum`. The time complexity is $O(N \log N)$ due to the initial sorting step, and the space complexity is $O(N)$ to store the result and the sorted list.
"""

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        sub_sum = 0
        ans = []
        for x in nums:
            sub_sum += x
            total_sum -= x
            ans.append(x)
            if sub_sum > total_sum:
                break
        return ans