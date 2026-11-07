# Relative Ranks
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Sorting, Heap (Priority Queue)

"""
The algorithm sorts the scores in descending order and maps each score to its corresponding rank—assigning "Gold Medal", "Silver Medal", "Bronze Medal" to the top three, and the numeric string of the position for the rest. Finally, it constructs the result list by looking up the original scores in this hash map. This approach operates with a **$O(N \log N)$** time complexity due to sorting and uses **$O(N)$** space to store the rank mapping and output list.
"""

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        return [rank_map[s] for s in score]