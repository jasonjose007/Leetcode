# Gas Station
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Greedy

"""
This solution uses a greedy algorithm to find the starting gas station by first checking if the total gas is at least the total cost, which guarantees a solution exists. It then iterates through the stations, keeping a running sum of the net gas (`gas[i] - cost[i]`); whenever this sum drops below zero, it resets the starting point to the next station and clears the running total. This efficient approach runs in **$O(n)$ time** and uses **$O(1)$ space**.
"""

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start