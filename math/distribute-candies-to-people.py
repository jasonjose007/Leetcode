# Distribute Candies to People
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Simulation

"""
This algorithm directly simulates the candy distribution by looping in a round-robin fashion (`i % num_people`) and giving an incrementally increasing amount of candies (`current_candy`) to each person until all candies are exhausted. 

The time complexity is $O(\sqrt{\text{candies}})$ because the sum of distributed candies grows quadratically ($1 + 2 + \dots + k \approx \text{candies}$), taking roughly $\sqrt{2 \cdot \text{candies}}$ iterations to complete. The auxiliary space complexity is $O(\text{num\_people})$ to store and return the output list representing each person's candies.
"""

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = [0] * num_people
        i = 0
        current_candy = 1
        while candies > 0:
            give = min(candies, current_candy)
            ans[i % num_people] += give
            candies -= give
            current_candy += 1
            i += 1
        return ans